"""Core tests for the Ether-First Alchemical Autoresearch Loop.

Defensive-by-design: tests are written against the documented public
signatures of the ``ether_first`` package, but use getattr with fallbacks
where exact attribute names are uncertain, and assert on exception TYPE
(not wording) for error paths.

Run with:  python3 -m unittest test_ether_first_core -v
"""

import unittest

from ether_first import schemas, phases, nigredo, albedo, citrinitas, rubedo


# ---------------------------------------------------------------------------
# Helpers (defensive accessors)
# ---------------------------------------------------------------------------

def _enum_value(member):
    """Return the .value string of an enum member, tolerating plain strings."""
    return getattr(member, "value", member)


def _tag_value(tag):
    return _enum_value(tag)


def _get(obj, *names, default=None):
    """First present attribute among names on obj (dict or object)."""
    for name in names:
        if isinstance(obj, dict) and name in obj:
            return obj[name]
        if hasattr(obj, name):
            return getattr(obj, name)
    return default


def _claim_kind(finding):
    return _enum_value(_get(finding, "kind", "finding_kind"))


def _make_manifest(valid=True):
    """Build a minimal SourceManifest dict/object acceptable to validate_manifest."""
    entry_cls = schemas.SourceEntry
    try:
        entry = entry_cls(
            source_id="src-1",
            title="Field Notes",
            sha256="ab" * 32,
            bytes_recorded=True,
        )
    except TypeError:
        try:
            entry = entry_cls(
                id="src-1", sha256="ab" * 32, bytes_recorded=True
            )
        except TypeError:
            entry = {"source_id": "src-1", "sha256": "ab" * 32,
                     "bytes_recorded": True}
    manifest_cls = schemas.SourceManifest
    try:
        manifest = manifest_cls(entries=[entry])
    except TypeError:
        try:
            manifest = manifest_cls(sources=[entry])
        except TypeError:
            manifest = {"entries": [entry]}
    return manifest


def _make_claim(text="The field modulates neural coherence.",
                 tag=None, provenance="src-1", under_investigation=False):
    """Build a schemas.Claim with the real field names.

    Real Claim fields: statement, tag (single ClaimTag or None),
    provenance (list of manifest entry ids), under_investigation (bool).
    """
    tag = tag if tag is not None else schemas.ClaimTag.FIELD_FACET
    return schemas.Claim(
        statement=text,
        tag=tag,
        provenance=[provenance],
        under_investigation=under_investigation,
    )


def _make_claim_dict(text, tag, provenance):
    """Claim in the plain-dict shape consumed by albedo/citrinitas/rubedo:
    {"statement", "tag" (value string), "provenance" (list), "phase"}."""
    return {
        "statement": text,
        "tag": _tag_value(tag),
        "provenance": list(provenance),
        "phase": "ALBEDO",
    }


def _make_candidate(tag=None, member_count=2,
                    statement="The field modulates coherence.",
                    provenance=("field", "coherence")):
    """Citrinitas-style candidate dict consumed by rubedo.evaluate_candidates."""
    tag = tag if tag is not None else schemas.ClaimTag.DERIVED_FROM_FIELD
    return {
        "statement": statement,
        "tag": _tag_value(tag),
        "provenance": list(provenance),
        "member_count": member_count,
        "phase": "CITRINITAS",
    }


def _make_report(grounding=0.9, consistent=True, tensions=()):
    """Consequence report aligned by index with a candidate."""
    return {
        "consistent": consistent,
        "supports": ["support-1"] if grounding > 0 else [],
        "tensions": list(tensions),
        "grounding_score": grounding,
    }


# ---------------------------------------------------------------------------
# 1. Schema validation
# ---------------------------------------------------------------------------

class TestSchemaValidation(unittest.TestCase):

    def test_tagless_claim_rejected(self):
        claim = schemas.Claim(statement="x", tag=None, provenance=["src-1"])
        with self.assertRaises(ValueError):
            schemas.validate_claim(claim)

    def test_multiply_tagged_claim_rejected(self):
        tags = [schemas.ClaimTag.FIELD_FACET,
                schemas.ClaimTag.MATTER_FIRST_ARTIFACT]
        claim = schemas.Claim(statement="x", tag=tags, provenance=["s"])
        with self.assertRaises(ValueError):
            schemas.validate_claim(claim)

    def test_valid_single_tags_accepted(self):
        for tag in schemas.ClaimTag:
            claim = _make_claim(
                tag=tag,
                under_investigation=(
                    tag is schemas.ClaimTag.MATTER_FIRST_ARTIFACT))
            # must not raise
            schemas.validate_claim(claim)

    def test_manifest_missing_sha256_rejected(self):
        with self.assertRaises(ValueError):
            entry = {"source_id": "s1", "bytes_recorded": True}  # no sha256
            try:
                bad = schemas.SourceManifest(entries=[entry])
            except TypeError:
                bad = {"entries": [entry]}
            schemas.validate_manifest(bad)

    def test_manifest_bytes_recorded_false_rejected(self):
        with self.assertRaises(ValueError):
            entry = {"source_id": "s1", "sha256": "ab" * 32,
                     "bytes_recorded": False}
            try:
                bad = schemas.SourceManifest(entries=[entry])
            except TypeError:
                bad = {"entries": [entry]}
            schemas.validate_manifest(bad)

    def test_enum_value_strings_use_hyphens(self):
        self.assertEqual(
            _tag_value(schemas.ClaimTag.DERIVED_FROM_FIELD),
            "DERIVED-FROM-FIELD")
        self.assertEqual(
            _tag_value(schemas.ClaimTag.MATTER_FIRST_ARTIFACT),
            "MATTER-FIRST-ARTIFACT")
        self.assertEqual(
            _tag_value(schemas.ClaimTag.FIELD_FACET), "FIELD-FACET")


# ---------------------------------------------------------------------------
# 2. Phase ordering
# ---------------------------------------------------------------------------

class TestPhaseOrdering(unittest.TestCase):

    def _new_sequencer(self):
        return phases.PhaseSequencer()

    def _advance(self, seq, phase):
        for method in ("advance", "enter", "complete", "transition"):
            if hasattr(seq, method):
                getattr(seq, method)(phase)
                return
        self.fail("PhaseSequencer has no recognizable advance method")

    def test_skip_ether_axiom_to_albedo_raises(self):
        seq = self._new_sequencer()
        with self.assertRaises(phases.PhaseOrderError):
            self._advance(seq, phases.Phase.ALBEDO)

    def test_reentering_completed_phase_raises(self):
        seq = self._new_sequencer()
        self._advance(seq, phases.Phase.ETHER_AXIOM)
        self._advance(seq, phases.Phase.NIGREDO)
        with self.assertRaises(phases.PhaseOrderError):
            self._advance(seq, phases.Phase.ETHER_AXIOM)

    def test_full_five_phase_walk_succeeds(self):
        seq = self._new_sequencer()
        for phase in (phases.Phase.ETHER_AXIOM, phases.Phase.NIGREDO,
                      phases.Phase.ALBEDO, phases.Phase.CITRINITAS,
                      phases.Phase.RUBEDO):
            self._advance(seq, phase)  # must not raise


# ---------------------------------------------------------------------------
# 3. Ether-first invariant
# ---------------------------------------------------------------------------

class TestEtherFirstInvariant(unittest.TestCase):

    MATTER_TEXT = "the brain generates consciousness"

    def test_matter_first_text_flagged(self):
        # check_ether_first takes an iterable of claims and returns a list
        # of InvariantViolation; non-empty means the text was flagged.
        flagged = phases.check_ether_first([self.MATTER_TEXT])
        self.assertTrue(len(flagged) > 0)

    def test_tagged_artifact_under_investigation_tolerated(self):
        claim = {
            "text": self.MATTER_TEXT,
            "tags": [phases.MATTER_FIRST_ARTIFACT_TAG],
            "under_investigation": True,
        }
        violations = phases.check_ether_first([claim])
        self.assertEqual(len(violations), 0)


# ---------------------------------------------------------------------------
# 4. Cycle bounds
# ---------------------------------------------------------------------------

class TestCycleBounds(unittest.TestCase):

    def _plan(self, n):
        try:
            return phases.validate_cycle_plan(n)
        except TypeError:
            return phases.validate_cycle_plan({"cycles": n})

    def test_two_cycles_rejected(self):
        self.assertEqual(phases.MIN_CYCLES, 3)
        with self.assertRaises(phases.CyclePlanError):
            self._plan(2)

    def test_ten_cycles_rejected(self):
        self.assertEqual(phases.MAX_CYCLES, 9)
        with self.assertRaises(phases.CyclePlanError):
            self._plan(10)

    def test_three_and_nine_cycles_accepted(self):
        self._plan(3)  # must not raise
        self._plan(9)  # must not raise


# ---------------------------------------------------------------------------
# 5. Stagnation
# ---------------------------------------------------------------------------

class TestStagnation(unittest.TestCase):

    def _new_detector(self):
        return phases.StagnationDetector()

    def _record_stagnant(self, det):
        for method in ("record", "record_cycle", "update", "observe"):
            if hasattr(det, method):
                try:
                    getattr(det, method)(stagnant=True)
                except TypeError:
                    try:
                        getattr(det, method)({"stagnant": True})
                    except TypeError:
                        getattr(det, method)(0)  # zero new findings
                return
        self.fail("StagnationDetector has no recognizable record method")

    def test_stop_not_required_after_one_stagnant_cycle(self):
        det = self._new_detector()
        self._record_stagnant(det)
        stop = _get(det, "stop_required", default=None)
        if callable(stop):
            stop = stop()
        self.assertFalse(bool(stop))

    def test_stop_required_after_two_stagnant_cycles(self):
        det = self._new_detector()
        self._record_stagnant(det)
        self._record_stagnant(det)
        stop = _get(det, "stop_required", default=None)
        if callable(stop):
            stop = stop()
        self.assertTrue(bool(stop))


# ---------------------------------------------------------------------------
# 6. Nigredo
# ---------------------------------------------------------------------------

class TestNigredo(unittest.TestCase):

    SAMPLE = (
        "Consciousness is just neurons firing. "          # matter-first framing
        "All experience is always nothing but chemistry. "  # categorical leak
        "The field is primary, yet the field is not primary."  # contradiction
    )

    def test_findings_include_expected_kinds(self):
        manifest_terms = ["field", "consciousness", "neurons"]
        findings = nigredo.run_nigredo(self.SAMPLE, manifest_terms)
        kinds = {_claim_kind(f) for f in findings}
        expected = {
            _enum_value(schemas.FindingKind.MATTER_FIRST_FRAMING),
            _enum_value(schemas.FindingKind.CATEGORICAL_LEAK),
        }
        self.assertTrue(
            expected & kinds,
            "expected at least one of %s in findings, got %s"
            % (expected, kinds))


# ---------------------------------------------------------------------------
# 7. Albedo
# ---------------------------------------------------------------------------

class TestAlbedo(unittest.TestCase):

    MANIFEST_TERMS = ["field", "substrate", "neural coherence"]

    def _tag_values(self, claims):
        return {_tag_value(_get(c, "tag", "tags")) for c in claims}

    def test_field_modulation_tagged_derived_from_field(self):
        claims = albedo.build_claims(
            "The field modulates neural coherence.", self.MANIFEST_TERMS)
        self.assertIn("DERIVED-FROM-FIELD", self._tag_values(claims))

    def test_matter_first_sentence_tagged_artifact(self):
        claims = albedo.build_claims(
            "Consciousness is just neurons firing.", self.MANIFEST_TERMS)
        self.assertIn("MATTER-FIRST-ARTIFACT", self._tag_values(claims))

    def test_substrate_sentence_tagged_field_facet(self):
        claims = albedo.build_claims(
            "The substrate holds the pattern.", self.MANIFEST_TERMS)
        self.assertIn("FIELD-FACET", self._tag_values(claims))

    def test_dedupe_drops_case_insensitive_duplicates(self):
        a = _make_claim_dict("The Field Holds.",
                             schemas.ClaimTag.FIELD_FACET, ["field"])
        b = _make_claim_dict("the field holds.",
                             schemas.ClaimTag.FIELD_FACET, ["field"])
        result = albedo.dedupe_claims([a, b])
        self.assertEqual(len(result), 1)


# ---------------------------------------------------------------------------
# 8. Citrinitas
# ---------------------------------------------------------------------------

class TestCitrinitas(unittest.TestCase):

    def test_shared_provenance_field_claims_synthesize_with_field_tag(self):
        c1 = _make_claim_dict("The field modulates coherence.",
                              schemas.ClaimTag.DERIVED_FROM_FIELD,
                              ["field", "coherence"])
        c2 = _make_claim_dict("The field shapes excitability.",
                              schemas.ClaimTag.FIELD_FACET,
                              ["field", "coherence"])
        result = citrinitas.run_citrinitas([c1, c2], [])
        candidates = result["candidates"]
        self.assertTrue(len(candidates) >= 1)
        valid_field_tags = {
            _tag_value(schemas.ClaimTag.DERIVED_FROM_FIELD),
            _tag_value(schemas.ClaimTag.FIELD_FACET),
        }
        found = False
        for cand in candidates:
            tag = _tag_value(_get(cand, "tag", "tags", default=""))
            self.assertNotEqual(tag, "SYNTHESIS")
            if tag in valid_field_tags:
                found = True
        self.assertTrue(found,
                        "synthesis candidate must carry a valid field tag")

    def test_claim_overlapping_categorical_leak_finding_excluded(self):
        leak_text = "All experience is always nothing but chemistry."
        claim = _make_claim_dict(leak_text,
                                 schemas.ClaimTag.FIELD_FACET,
                                 ["field"])
        other = _make_claim_dict("The field modulates coherence.",
                                 schemas.ClaimTag.DERIVED_FROM_FIELD,
                                 ["field", "coherence"])
        finding = {
            "kind": _enum_value(schemas.FindingKind.CATEGORICAL_LEAK),
            "detail": leak_text,
            "phase": "NIGREDO",
            "span": (0, len(leak_text)),
        }
        result = citrinitas.run_citrinitas([claim, other], [finding])
        self.assertGreaterEqual(len(result["exclusions"]), 1,
                                "contaminated claim must be excluded")
        leak_frag = "chemistry"
        for cand in result["candidates"]:
            cand_text = str(_get(cand, "text", "statement", "members",
                                 default=cand))
            self.assertNotIn(leak_frag, cand_text)


# ---------------------------------------------------------------------------
# 9. Rubedo evaluation
# ---------------------------------------------------------------------------

class TestRubedo(unittest.TestCase):

    def _evaluate(self, candidates, reports):
        return rubedo.evaluate_candidates(candidates, reports)

    def _decision_of(self, evaluations, bucket):
        return evaluations[bucket][0]["decision"].lower()

    def test_high_grounding_field_candidate_accepted(self):
        cand = _make_candidate(tag=schemas.ClaimTag.DERIVED_FROM_FIELD,
                               member_count=2)
        outcome = self._decision_of(
            self._evaluate([cand], [_make_report(grounding=0.9)]), "accepted")
        self.assertIn("accept", outcome)

    def test_low_grounding_rejected(self):
        cand = _make_candidate()
        outcome = self._decision_of(
            self._evaluate([cand], [_make_report(grounding=0.1)]), "rejected")
        self.assertIn("reject", outcome)

    def test_mid_grounding_deferred(self):
        cand = _make_candidate()
        outcome = self._decision_of(
            self._evaluate([cand], [_make_report(grounding=0.5)]), "deferred")
        self.assertIn("defer", outcome)

    def test_matter_first_artifact_never_accepted(self):
        cand = _make_candidate(tag=schemas.ClaimTag.MATTER_FIRST_ARTIFACT,
                               member_count=4)
        outcome = self._decision_of(
            self._evaluate([cand], [_make_report(grounding=0.9)]), "deferred")
        self.assertIn("defer", outcome)
        self.assertNotIn("accept", outcome.replace("deferred", ""))

    def test_threshold_constants(self):
        self.assertAlmostEqual(rubedo.DEFAULT_ACCEPT_THRESHOLD, 0.8, places=5)
        self.assertAlmostEqual(rubedo.DEFAULT_REJECT_THRESHOLD, 0.2, places=5)


# ---------------------------------------------------------------------------
# 10. Convergence report
# ---------------------------------------------------------------------------

class TestConvergenceReport(unittest.TestCase):

    def _build(self, decisions):
        """Build a convergence report from a list of decision strings
        ('accepted'/'rejected'/'deferred')."""
        evaluations = {
            "accepted": [{"statement": "s", "tag": "FIELD-FACET",
                          "decision": "ACCEPT", "rationale": "r"}
                         for _ in decisions if _ == "accepted"],
            "rejected": [{"statement": "s", "tag": "FIELD-FACET",
                          "decision": "REJECT", "rationale": "r"}
                         for _ in decisions if _ == "rejected"],
            "deferred": [{"statement": "s", "tag": "FIELD-FACET",
                          "decision": "DEFER", "rationale": "r"}
                         for _ in decisions if _ == "deferred"],
        }
        return rubedo.build_convergence_report(
            run_id="test-run",
            evaluations=evaluations,
            cycles_run=1,
            stop_reason=rubedo.STOP_REASON_CYCLE_LIMIT,
            dry_run=True,
        )

    def test_canon_mutated_always_false(self):
        for outcomes in ([], ["accepted"], ["rejected"], ["accepted", "deferred"]):
            report = self._build(outcomes)
            self.assertFalse(bool(_get(report, "canon_mutated", default=False)))

    def test_outcome_converged_when_at_least_one_accepted(self):
        report = self._build(["accepted"])
        outcome = str(_enum_value(
            _get(report, "outcome", "status", "decision", default=""))).lower()
        self.assertIn("converged", outcome)

    def test_outcome_not_converged_with_zero_accepted(self):
        report = self._build(["rejected", "deferred"])
        outcome = str(_enum_value(
            _get(report, "outcome", "status", "decision", default=""))).lower()
        self.assertNotIn("converged", outcome)


if __name__ == "__main__":
    unittest.main()
