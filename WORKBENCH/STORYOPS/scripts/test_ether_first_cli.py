#!/usr/bin/env python3
"""CLI + artifact + safety integration tests for the Ether-First loop.

Scope (issue #1, Phase 4): subprocess CLI runs of ether_first_loop.py and
manifest.py, artifact layout/completeness, dry-run canon safety, artifact
reproducibility, manifest immutability, phase ordering, termination bound,
and defensive-import guards. Core-module unit tests live in
test_ether_first_core.py (sibling deliverable) and are out of scope here.

Run from WORKBENCH/STORYOPS/scripts/:
    python3 -m unittest test_ether_first_cli -v
or discover from repo root:
    python3 -m unittest discover -s WORKBENCH/STORYOPS/scripts -p "test_ether_first_cli.py"
"""
from __future__ import annotations

import hashlib
import inspect
import json
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parents[2]
LOOP_CLI = SCRIPTS_DIR / "ether_first_loop.py"
MANIFEST_CLI = SCRIPTS_DIR / "ether_first" / "manifest.py"

CHAPTER_1 = REPO_ROOT / "CHAPTERS" / "book_1" / "Chapter-01-The-Choroid-Plexus.md"
CHAPTER_14 = REPO_ROOT / "CHAPTERS" / "book_2" / "Chapter-14-The-Three-Body-Coordination.md"
CHAPTERS = [CHAPTER_1, CHAPTER_14]

PHASE_ORDER = ["ETHER_AXIOM", "NIGREDO", "ALBEDO", "CITRINITAS", "RUBEDO"]

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from ether_first import artifacts, manifest as manifest_mod  # noqa: E402


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _run_cli(argv: list, cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable] + [str(a) for a in argv],
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
        timeout=120,
    )


class CliTestBase(unittest.TestCase):
    """Shared fixture: tempdir + a real 2-chapter manifest built in-process."""

    def setUp(self) -> None:
        for ch in CHAPTERS:
            if not ch.is_file():
                self.fail(f"required chapter fixture missing: {ch}")
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.manifest_path = self.base / "manifest.json"
        manifest = manifest_mod.build_manifest(
            [(str(ch), "canon") for ch in CHAPTERS],
            "ether-first-manifest-v1",
        )
        manifest_mod.save_manifest(manifest, self.manifest_path)
        self.manifest = manifest

    def run_loop(self, extra: list | None = None, base: Path | None = None) -> subprocess.CompletedProcess:
        argv = [LOOP_CLI, "--manifest", self.manifest_path,
                "--base", base or (self.base / "runs")]
        argv.extend(extra or [])
        result = _run_cli(argv, cwd=self.base)
        self.assertEqual(result.returncode, 0,
                         f"loop CLI failed\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}")
        return result

    @staticmethod
    def single_run_dir(base: Path) -> Path:
        runs = [p for p in base.iterdir() if p.is_dir()]
        assert len(runs) == 1, f"expected exactly 1 run dir in {base}, got {runs}"
        return runs[0]

    @staticmethod
    def load_report(run_dir: Path) -> dict:
        with open(run_dir / "convergence-report.json", encoding="utf-8") as f:
            return json.load(f)


class TestManifestCli(CliTestBase):
    def test_build_and_validate_two_chapters(self):
        out = self.base / "cli-manifest.json"
        build = _run_cli(
            [MANIFEST_CLI, "build", "--out", out,
             "--canon", str(CHAPTER_1), str(CHAPTER_14)],
            cwd=self.base,
        )
        self.assertEqual(build.returncode, 0, build.stderr)
        self.assertTrue(out.is_file())

        validate = _run_cli([MANIFEST_CLI, "validate", out], cwd=self.base)
        self.assertEqual(validate.returncode, 0, validate.stderr)
        self.assertIn("VALID", validate.stdout)
        self.assertIn("2 entries", validate.stdout)

        manifest = manifest_mod.load_manifest(out)
        self.assertEqual(manifest["entry_count"], 2)
        for entry, chapter in zip(manifest["entries"], CHAPTERS):
            self.assertEqual(entry["path"], str(chapter))
            self.assertEqual(entry["role"], "canon")
            self.assertEqual(entry["sha256"], _sha256(chapter))
            self.assertTrue(entry["bytes_recorded"])

    def test_tampered_sha256_detected_by_rehash(self):
        tampered = json.loads(json.dumps(self.manifest))
        digest = tampered["entries"][0]["sha256"]
        replacement = "0" if digest[0] != "0" else "1"
        tampered["entries"][0]["sha256"] = replacement + digest[1:]
        bad_path = self.base / "tampered.json"
        manifest_mod.save_manifest(tampered, bad_path)

        # validate_manifest is structural only; verify_manifest re-hashes
        # source bytes against the pinned sha256 and catches the tampering.
        manifest_mod.validate_manifest(tampered)
        entry = tampered["entries"][0]
        self.assertNotEqual(
            _sha256(Path(entry["path"])), entry["sha256"],
            "tampered manifest sha256 must not match source bytes on disk",
        )
        with self.assertRaises(ValueError):
            manifest_mod.verify_manifest(tampered)

        # The loop CLI now runs verify_manifest: a sha256 flip fails the run.
        result = _run_cli([LOOP_CLI, "--manifest", bad_path,
                           "--base", self.base / "runs"], cwd=self.base)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid manifest", result.stderr)

    def test_bytes_recorded_false_rejected(self):
        tampered = json.loads(json.dumps(self.manifest))
        tampered["entries"][0]["bytes_recorded"] = False
        bad_path = self.base / "tampered-bytes.json"
        manifest_mod.save_manifest(tampered, bad_path)

        result = _run_cli([LOOP_CLI, "--manifest", bad_path,
                           "--base", self.base / "runs"], cwd=self.base)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid manifest", result.stderr)


class TestDryRunSafety(CliTestBase):
    def test_dry_run_leaves_canon_untouched(self):
        hashes_before = {ch: _sha256(ch) for ch in CHAPTERS}

        result = self.run_loop(["--cycles", "3"])
        run_dir = self.single_run_dir(self.base / "runs")
        report = self.load_report(run_dir)

        self.assertTrue(report["dry_run"], "report must record dry_run: true")
        self.assertFalse(report["canon_mutated"], "report must record canon_mutated: false")
        self.assertIn("dry-run", result.stdout)

        for ch, before in hashes_before.items():
            self.assertEqual(_sha256(ch), before,
                             f"canon chapter mutated by dry run: {ch}")

    def test_apply_flag_still_never_mutates_canon(self):
        hashes_before = {ch: _sha256(ch) for ch in CHAPTERS}

        result = self.run_loop(["--cycles", "3", "--apply"])
        run_dir = self.single_run_dir(self.base / "runs")
        report = self.load_report(run_dir)

        self.assertFalse(report["dry_run"])
        self.assertFalse(report["canon_mutated"], "--apply must never mutate canon")
        self.assertIn("apply", result.stdout)

        for ch, before in hashes_before.items():
            self.assertEqual(_sha256(ch), before,
                             f"canon chapter mutated under --apply: {ch}")


class TestArtifactCompleteness(CliTestBase):
    def test_all_contract_artifacts_exist(self):
        self.run_loop(["--cycles", "3"])
        run_dir = self.single_run_dir(self.base / "runs")

        self.assertTrue((run_dir / "source-manifest.json").is_file())
        for phase in PHASE_ORDER:
            self.assertTrue((run_dir / "phase-packets" / f"{phase}.json").is_file(),
                            f"missing phase packet: {phase}")
        self.assertTrue((run_dir / "candidate-ledger.jsonl").is_file())
        self.assertTrue((run_dir / "evaluator-ledger.jsonl").is_file())
        self.assertTrue((run_dir / "scorecards" / "cycle-1.json").is_file())
        self.assertTrue((run_dir / "convergence-report.json").is_file())
        self.assertTrue((run_dir / "convergence-report.md").is_file())

        md = (run_dir / "convergence-report.md").read_text(encoding="utf-8")
        self.assertIn("Convergence Report", md)
        self.assertIn("dry_run", md)

        pinned = manifest_mod.load_manifest(run_dir / "source-manifest.json")
        self.assertEqual(pinned, self.manifest,
                         "pinned source-manifest.json must equal the input manifest")

    def test_run_dir_naming_scheme(self):
        self.run_loop(["--cycles", "3"])
        run_dir = self.single_run_dir(self.base / "runs")
        stamp, _, suffix = run_dir.name.partition("-")
        self.assertEqual(len(stamp), 16)
        self.assertTrue(stamp.endswith("Z"))
        self.assertEqual(suffix, artifacts.manifest_hash(self.manifest))


class TestArtifactReproducibility(CliTestBase):
    @staticmethod
    def _normalize_run_id(obj):
        if isinstance(obj, dict):
            return {
                k: ("<RUN_ID>" if k == "run_id" else TestArtifactReproducibility._normalize_run_id(v))
                for k, v in obj.items()
            }
        if isinstance(obj, list):
            return [TestArtifactReproducibility._normalize_run_id(v) for v in obj]
        return obj

    def test_identical_manifest_reproduces_artifacts(self):
        base_a, base_b = self.base / "runs-a", self.base / "runs-b"
        self.run_loop(["--cycles", "3"], base=base_a)
        time.sleep(1.1)  # run-id timestamp resolution is 1s
        self.run_loop(["--cycles", "3"], base=base_b)
        run_a = self.single_run_dir(base_a)
        run_b = self.single_run_dir(base_b)

        self.assertNotEqual(run_a.name, run_b.name,
                            "run ids must differ (timestamp + manifest hash scheme)")

        for phase in PHASE_ORDER:
            with open(run_a / "phase-packets" / f"{phase}.json", encoding="utf-8") as f:
                packet_a = json.load(f)
            with open(run_b / "phase-packets" / f"{phase}.json", encoding="utf-8") as f:
                packet_b = json.load(f)
            self.assertEqual(packet_a, packet_b, f"phase packet {phase} not reproducible")

        report_a = self._normalize_run_id(self.load_report(run_a))
        report_b = self._normalize_run_id(self.load_report(run_b))
        self.assertEqual(report_a, report_b,
                         "convergence reports must match after run_id normalization")

        for name in ("candidate-ledger.jsonl", "evaluator-ledger.jsonl"):
            self.assertEqual(
                (run_a / name).read_text(encoding="utf-8"),
                (run_b / name).read_text(encoding="utf-8"),
                f"{name} not byte-identical across runs",
            )


class TestManifestImmutability(CliTestBase):
    def test_source_manifest_written_exactly_once(self):
        run_dir = artifacts.new_run_dir(self.base / "immut", self.manifest)
        artifacts.write_source_manifest(run_dir, self.manifest)
        with self.assertRaises(FileExistsError):
            artifacts.write_source_manifest(run_dir, self.manifest)


class TestPhaseOrder(CliTestBase):
    def test_phase_packets_exist_in_contract_order_with_matching_names(self):
        self.run_loop(["--cycles", "3"])
        run_dir = self.single_run_dir(self.base / "runs")

        packet_files = sorted(p.name for p in (run_dir / "phase-packets").glob("*.json"))
        self.assertEqual(packet_files, sorted(f"{p}.json" for p in PHASE_ORDER))

        for phase in PHASE_ORDER:
            with open(run_dir / "phase-packets" / f"{phase}.json", encoding="utf-8") as f:
                packet = json.load(f)
            self.assertEqual(packet["phase"], phase,
                             f"phase field mismatch in {phase}.json")

        report = self.load_report(run_dir)
        self.assertEqual(report["phases"], PHASE_ORDER,
                         "report must record phases in strict alchemical order")


class TestTerminationBound(CliTestBase):
    def _assert_bounded(self, requested: int, expected_effective: int):
        self.run_loop(["--cycles", str(requested)])
        run_dir = self.single_run_dir(self.base / "runs")
        report = self.load_report(run_dir)

        self.assertLessEqual(report["cycles_run"], expected_effective)
        self.assertGreaterEqual(report["cycles_run"], 1)
        self.assertTrue(report["stop_reason"], "stop_reason must be recorded")

        scorecards = sorted((run_dir / "scorecards").glob("cycle-*.json"))
        self.assertEqual(len(scorecards), report["cycles_run"],
                         "scorecard count must match cycles_run")

    def test_cycles_3(self):
        self._assert_bounded(requested=3, expected_effective=3)

    def test_cycles_9(self):
        self._assert_bounded(requested=9, expected_effective=9)


class TestMissingModuleFallback(unittest.TestCase):
    """Pragmatic option: static inspection of the defensive-import guards in
    ether_first_loop.py (per task spec), rather than env-hacking subprocesses."""

    def test_defensive_import_guards_present(self):
        import ether_first_loop

        source = inspect.getsource(ether_first_loop)
        self.assertGreaterEqual(source.count("except ImportError"), 3,
                                "expected defensive ImportError guards for sibling modules")
        for module in ("nigredo", "albedo", "citrinitas", "rubedo"):
            self.assertIn(module, source)

    def test_loop_runs_when_phase_modules_hidden(self):
        """Functional fallback proof: subprocess with a stub ether_first package
        (schemas/phases/manifest/artifacts re-exported; phase modules absent)."""
        scripts_src = SCRIPTS_DIR / "ether_first"
        reexport = {"schemas", "phases", "manifest", "artifacts"}
        hidden = {"nigredo", "albedo", "citrinitas", "rubedo"}

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            stub_root = tmp_path / "stubsrc"
            stub_pkg = stub_root / "ether_first"
            stub_pkg.mkdir(parents=True)
            (stub_pkg / "__init__.py").write_text("", encoding="utf-8")
            for name in reexport:
                (stub_pkg / f"{name}.py").write_text(
                    f"from ether_first_real.{name} import *  # noqa: F401,F403\n",
                    encoding="utf-8",
                )
            real_pkg = stub_root / "ether_first_real"
            real_pkg.mkdir()
            (real_pkg / "__init__.py").write_text("", encoding="utf-8")
            for name in reexport:
                (real_pkg / f"{name}.py").write_text(
                    (scripts_src / f"{name}.py").read_text(encoding="utf-8"),
                    encoding="utf-8",
                )
            for name in hidden:
                self.assertFalse((stub_pkg / f"{name}.py").exists())

            manifest_path = tmp_path / "manifest.json"
            manifest_mod.save_manifest(
                manifest_mod.build_manifest(
                    [(str(ch), "canon") for ch in CHAPTERS],
                    "ether-first-manifest-v1",
                ),
                manifest_path,
            )

            wrapper = stub_root / "run_stubbed.py"
            wrapper.write_text(
                "import sys\n"
                f"sys.path.insert(0, {str(stub_root)!r})\n"
                "import ether_first, ether_first_real\n"
                "sys.modules['ether_first'] = ether_first\n"
                f"sys.path.insert(0, {str(SCRIPTS_DIR)!r})\n"
                f"sys.argv = ['ether_first_loop.py', '--manifest', {str(manifest_path)!r}, "
                f"'--cycles', '3', '--base', {str(tmp_path / 'runs')!r}]\n"
                "for mod in ('nigredo', 'albedo', 'citrinitas', 'rubedo'):\n"
                "    assert not hasattr(ether_first, mod), mod\n"
                "import runpy\n"
                "runpy.run_path('WORKBENCH_MARKER', run_name='__main__')\n",
                encoding="utf-8",
            )
            wrapper.write_text(
                wrapper.read_text(encoding="utf-8").replace(
                    "'WORKBENCH_MARKER'", repr(str(LOOP_CLI))
                ),
                encoding="utf-8",
            )
            result = _run_cli([wrapper], cwd=tmp_path)
            self.assertEqual(result.returncode, 0,
                             f"stubbed-package run failed\nstdout:\n{result.stdout}\n"
                             f"stderr:\n{result.stderr}")

            run_dir = next((tmp_path / "runs").iterdir())
            report = json.loads((run_dir / "convergence-report.json").read_text(encoding="utf-8"))
            self.assertEqual(report["modules_loaded"],
                             {"nigredo": False, "albedo": False,
                              "citrinitas": False, "rubedo": False})
            for phase in PHASE_ORDER:
                packet = json.loads(
                    (run_dir / "phase-packets" / f"{phase}.json").read_text(encoding="utf-8"))
                self.assertTrue(packet["stub"], f"{phase} must fall back to stub packet")


if __name__ == "__main__":
    unittest.main()
