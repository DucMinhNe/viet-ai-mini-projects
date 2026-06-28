import csv
import importlib.util
import unittest
from pathlib import Path


MAIN_PATH = Path(__file__).resolve().parents[1] / "main.py"
spec = importlib.util.spec_from_file_location("voice_main", MAIN_PATH)
voice_main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(voice_main)


class ClassifyTests(unittest.TestCase):
    def test_keyword_does_not_match_inside_a_word(self):
        # "ngoi" (to sit) contains "goi", a calendar_reminder keyword.
        # It must not trigger that intent.
        intent, confidence = voice_main.classify("toi muon ngoi nghi mot chut")
        self.assertEqual(intent, "unknown")
        self.assertEqual(confidence, 0.0)

    def test_labelled_dataset_still_classifies_correctly(self):
        rows = voice_main.load_samples(voice_main.DATA_PATH)
        for row in rows:
            intent, _ = voice_main.classify(row["transcript"])
            self.assertEqual(intent, row["expected_intent"], row["transcript"])


if __name__ == "__main__":
    unittest.main()
