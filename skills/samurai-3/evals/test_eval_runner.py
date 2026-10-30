import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import run_evals

class HarnessTests(unittest.TestCase):
    def test_fixture_is_diverse(self):
        cases=run_evals.load_cases()
        self.assertGreaterEqual(len(cases),12)
        self.assertGreaterEqual(len({c["role"] for c in cases}),8)
    def test_missing_fields_fail(self):
        problems=run_evals.evaluate({"case_id":"E01","decision":"STOP"}, {"E01"})
        self.assertTrue(any(x.startswith("missing:") for x in problems))
    def test_well_formed_response_passes_structure(self):
        r={"case_id":"E01","decision":"EXPERIMENT","evidence":["hypothesis"],
           "alternatives":["existing help"],"test":"compare a safe baseline",
           "risk":"misdiagnosis","owner":"authorized support lead",
           "text":"Working hypothesis and one next question."}
        self.assertEqual(run_evals.evaluate(r,{"E01"}),[])
    def test_unrecognized_decision_fails(self):
        self.assertIn("invalid decision",run_evals.evaluate(
            {"case_id":"E01","decision":"GUARANTEED"}, {"E01"}))

if __name__=="__main__":
    unittest.main()
