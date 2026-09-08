#!/usr/bin/env python3
from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from autoresearch_loop import run_loop
from gating_contract import evaluate_candidate_change, gating_contract


ROOT = Path(__file__).resolve().parents[3]
CHAPTER_6 = ROOT / "CHAPTERS" / "book_1" / "Chapter-06-The-Synaptic-Crossroads.md"


class TestCosmologyCR00Contract(unittest.TestCase):
    def test_contract_supersedes_unconditional_compression_ban(self):
        contract = gating_contract()

        self.assertNotIn(
            "non_additive_or_compressing_change",
            contract["stage_acceptance"]["reject_if"],
        )
        self.assertIn(
            "unjustified_compression_or_scene_spine_loss",
            contract["stage_acceptance"]["reject_if"],
        )

    def test_justified_compression_keeps_protected_choice(self):
        before = (
            "The shard vote completed. Gideon said yes. "
            "The corridor repeated the explanation twice."
        )
        after = "The shard vote completed. Gideon said yes."

        result = evaluate_candidate_change(
            before,
            after,
            "justified compression: action carries the repeated explanation",
            protected_choices=["Gideon said yes"],
        )

        self.assertTrue(result["accepted"])
        self.assertTrue(result["compressed"])

    def test_compression_rejects_missing_consequential_choice(self):
        before = "The shard vote completed. Gideon said yes."
        after = "The shard vote completed."

        result = evaluate_candidate_change(
            before,
            after,
            "justified compression: action carries the scene spine",
            protected_choices=["Gideon said yes"],
        )

        self.assertFalse(result["accepted"])
        self.assertEqual(result["missing_protected_choices"], ["Gideon said yes"])


class TestCosmologyCR00Runner(unittest.TestCase):
    def test_run_id_keeps_repeated_runs_distinct_and_dry(self):
        original = CHAPTER_6.read_bytes()

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            run_a = run_loop(
                CHAPTER_6,
                ["dedupe"],
                3,
                False,
                "CR-00-proof-a",
                tmp_path,
            )
            run_b = run_loop(
                CHAPTER_6,
                ["dedupe"],
                3,
                False,
                "CR-00-proof-b",
                tmp_path,
            )

            self.assertNotEqual(run_a["run_dir"], run_b["run_dir"])
            self.assertTrue((Path(run_a["run_dir"]) / "autoresearch-trace.json").exists())
            self.assertTrue((Path(run_b["run_dir"]) / "autoresearch-trace.json").exists())
            self.assertEqual(CHAPTER_6.read_bytes(), original)
            self.assertEqual(run_a["actual_cycles"], 1)

    def test_apply_mutates_only_supplied_temporary_copy(self):
        original = CHAPTER_6.read_bytes()

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            temp_chapter = tmp_path / "CHAPTERS" / "book_1" / CHAPTER_6.name
            temp_chapter.parent.mkdir(parents=True)
            shutil.copyfile(CHAPTER_6, temp_chapter)

            run_loop(
                temp_chapter,
                ["dedupe"],
                3,
                True,
                "CR-00-apply-proof",
                tmp_path / "runs",
            )

            self.assertEqual(CHAPTER_6.read_bytes(), original)
            self.assertTrue(temp_chapter.exists())


if __name__ == "__main__":
    unittest.main()
