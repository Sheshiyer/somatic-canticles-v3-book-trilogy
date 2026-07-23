import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from automation.ether_first.__main__ import build_parser, main
from automation.ether_first.config import load_config
from automation.ether_first.controller import (
    PHASES,
    build_source_manifest,
    evaluate_candidate,
    run_loop,
    validate_claim_tags,
)



class EtherFirstCliTests(unittest.TestCase):
    def test_cli_defaults_to_dry_run(self):
        self.assertTrue(build_parser().parse_args([]).dry_run)

    def test_cli_rejects_cycles_below_three(self):
        with self.assertRaises(SystemExit):
            build_parser().parse_args(["--cycles", "2"])

    def test_cli_rejects_cycles_above_nine(self):
        with self.assertRaises(SystemExit):
            build_parser().parse_args(["--cycles", "10"])

    def test_cli_accepts_config_path(self):
        arguments = build_parser().parse_args(["--config", "run.json"])

        self.assertEqual(arguments.config, Path("run.json"))

    def test_cli_runs_configured_candidates(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "canon.md"
            source.write_text("Ether is primary.", encoding="utf-8")
            config = root / "run.json"
            config.write_text(
                json.dumps(
                    {
                        "source_groups": {
                            "canon": ["canon.md"],
                            "approved-blog": [],
                            "selected-skill": [],
                            "cross-domain-reference": [],
                        },
                        "candidates": [
                            {
                                "id": "candidate-1",
                                "claim": "Matter is a field facet.",
                                "tags": ["FIELD-FACET"],
                                "field_grounding_passed": True,
                                "isa_probe_passed": True,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            artifacts_root = root / "artifacts"

            exit_code = main(
                [
                    "--config",
                    str(config),
                    "--artifacts-root",
                    str(artifacts_root),
                    "--run-id",
                    "configured",
                ]
            )

            ledger = json.loads(
                (artifacts_root / "ether-first-loop" / "configured" / "candidate-ledger.json").read_text(
                    encoding="utf-8"
                )
            )
        self.assertEqual(exit_code, 0)
        self.assertEqual(ledger["candidates"][0]["id"], "candidate-1")


class EtherFirstConfigTests(unittest.TestCase):
    def test_load_config_returns_sources_and_candidates(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source = root / "canon.md"
            source.write_text("Ether is primary.", encoding="utf-8")
            config = root / "run.json"
            config.write_text(
                json.dumps(
                    {
                        "source_groups": {
                            "canon": ["canon.md"],
                            "approved-blog": [],
                            "selected-skill": [],
                            "cross-domain-reference": [],
                        },
                        "candidates": [
                            {
                                "id": "candidate-1",
                                "claim": "Matter is a field facet.",
                                "tags": ["FIELD-FACET"],
                                "field_grounding_passed": True,
                                "isa_probe_passed": True,
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            loaded = load_config(config)

        self.assertEqual(loaded["source_groups"]["canon"], [source.resolve()])
        self.assertEqual(loaded["candidates"][0]["id"], "candidate-1")

    def test_load_config_rejects_invalid_json(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            config = Path(temporary_directory) / "run.json"
            config.write_text("{", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "valid JSON"):
                load_config(config)

    def test_load_config_rejects_missing_required_top_level_keys(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            config = Path(temporary_directory) / "run.json"
            config.write_text(
                json.dumps(
                    {
                        "source_groups": {
                            "canon": [],
                            "approved-blog": [],
                            "selected-skill": [],
                            "cross-domain-reference": [],
                        }
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "candidates"):
                load_config(config)

    def test_load_config_rejects_missing_source_path(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            config = Path(temporary_directory) / "run.json"
            config.write_text(
                json.dumps(
                    {
                        "source_groups": {
                            "canon": ["missing.md"],
                            "approved-blog": [],
                            "selected-skill": [],
                            "cross-domain-reference": [],
                        },
                        "candidates": [],
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "does not exist"):
                load_config(config)

    def test_load_config_rejects_missing_required_source_family(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            config = Path(temporary_directory) / "run.json"
            config.write_text(
                json.dumps(
                    {
                        "source_groups": {"canon": []},
                        "candidates": [],
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "source_groups must include"):
                load_config(config)

    def test_load_config_rejects_incomplete_candidate(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            config = Path(temporary_directory) / "run.json"
            config.write_text(
                json.dumps(
                    {
                        "source_groups": {
                            "canon": [],
                            "approved-blog": [],
                            "selected-skill": [],
                            "cross-domain-reference": [],
                        },
                        "candidates": [{"id": "candidate-1"}],
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "claim"):
                load_config(config)


class EtherFirstUnitTests(unittest.TestCase):
    def test_phase_order(self):
        self.assertEqual(
            PHASES,
            (
                "Phase 0: Ether Axiom",
                "Nigredo",
                "Albedo",
                "Citrinitas",
                "Rubedo",
            ),
        )

    def test_rejects_zero_claim_tags(self):
        with self.assertRaisesRegex(ValueError, "exactly one"):
            validate_claim_tags([])

    def test_rejects_multiple_claim_tags(self):
        with self.assertRaisesRegex(ValueError, "exactly one"):
            validate_claim_tags(["FIELD-FACET", "DERIVED-FROM-FIELD"])

    def test_manifest_records_provenance(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            sources = {}
            for provenance in (
                "canon",
                "approved-blog",
                "selected-skill",
                "cross-domain-reference",
            ):
                source_path = root / f"{provenance}.md"
                source_path.write_text(provenance, encoding="utf-8")
                sources[provenance] = [source_path]

            manifest = build_source_manifest(sources)

        self.assertEqual(
            {entry["provenance"] for entry in manifest["sources"]},
            set(sources),
        )
        self.assertTrue(all(entry["bytes"] > 0 for entry in manifest["sources"]))
        self.assertTrue(all(entry["id"].startswith("sha256:") for entry in manifest["sources"]))

    def test_candidate_requires_both_acceptance_probes(self):
        candidate = {
            "id": "candidate-acceptance",
            "claim": "Matter is a field facet.",
            "tags": ["FIELD-FACET"],
            "field_grounding_passed": True,
            "isa_probe_passed": True,
        }
        self.assertTrue(evaluate_candidate(candidate)["accepted"])
        candidate["field_grounding_passed"] = False
        self.assertFalse(evaluate_candidate(candidate)["accepted"])
        candidate["field_grounding_passed"] = True
        candidate["isa_probe_passed"] = False
        self.assertFalse(evaluate_candidate(candidate)["accepted"])

    def test_unsupported_substrate_claim_emits_categorical_leak(self):
        result = evaluate_candidate(
            {
                "id": "candidate-1",
                "claim": "Matter produces the field without substrate support.",
                "tags": ["MATTER-FIRST-ARTIFACT"],
                "field_grounding_passed": False,
                "isa_probe_passed": True,
            }
        )

        self.assertFalse(result["accepted"])
        self.assertEqual(result["findings"][0]["code"], "CATEGORICAL-LEAK")

    def test_matter_first_artifact_never_accepted_even_with_both_probes(self):
        result = evaluate_candidate(
            {
                "id": "candidate-matter-first-both-true",
                "claim": "Matter is primary and field is emergent.",
                "tags": ["MATTER-FIRST-ARTIFACT"],
                "field_grounding_passed": True,
                "isa_probe_passed": True,
            }
        )

        self.assertFalse(result["accepted"])
        self.assertEqual(result["findings"][0]["code"], "CATEGORICAL-LEAK")


class EtherFirstRunTests(unittest.TestCase):
    def test_run_writes_required_artifacts_without_mutating_sources(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source_path = root / "canon.md"
            source_path.write_text("Ether is primary.", encoding="utf-8")
            before = source_path.read_bytes()

            report = run_loop(
                source_groups={"canon": [source_path]},
                candidates=[
                    {
                        "id": "candidate-1",
                        "claim": "Matter is a field facet.",
                        "tags": ["FIELD-FACET"],
                        "field_grounding_passed": True,
                        "isa_probe_passed": True,
                    }
                ],
                cycles=3,
                artifacts_root=root / "artifacts",
                run_id="proof",
            )

            run_directory = report["run_directory"]
            self.assertEqual(source_path.read_bytes(), before)
            self.assertTrue(
                str(run_directory).startswith(str((root / "artifacts").resolve()))
            )
            self.assertTrue((run_directory / "manifest.json").is_file())
            self.assertTrue((run_directory / "candidate-ledger.json").is_file())
            self.assertTrue((run_directory / "evaluator-ledger.json").is_file())
            self.assertTrue((run_directory / "cycle-scorecard.json").is_file())
            self.assertTrue((run_directory / "convergence-report.json").is_file())
            for phase in PHASES:
                self.assertTrue((run_directory / "phase-packets" / f"{phase}.json").is_file())

    def test_run_stops_after_two_consecutive_stagnant_cycles(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            source_path = root / "canon.md"
            source_path.write_text("Ether is primary.", encoding="utf-8")

            report = run_loop(
                source_groups={"canon": [source_path]},
                candidates=[],
                cycles=9,
                artifacts_root=root / "artifacts",
                run_id="stagnant",
            )

        self.assertEqual(
            report["convergence"]["stop_reason"],
            "two_consecutive_stagnant_cycles",
        )
        self.assertEqual(report["convergence"]["cycles_executed"], 3)


if __name__ == "__main__":
    unittest.main()
