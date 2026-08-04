import importlib.util
import unittest
from pathlib import Path

MAIN_PATH = Path(__file__).resolve().parents[1] / "main.py"
spec = importlib.util.spec_from_file_location("assistant_main", MAIN_PATH)
assistant_main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assistant_main)


class ChooseModelTests(unittest.TestCase):
    def test_exact_match(self):
        models = ["llama3.2:latest", "gemma2:9b"]
        result = assistant_main.choose_model(models, "gemma2:9b")
        self.assertEqual(result, "gemma2:9b")

    def test_prefix_tag_match(self):
        models = ["llama3.2:latest", "qwen2.5:7b"]
        result = assistant_main.choose_model(models, "llama3.2")
        self.assertEqual(result, "llama3.2:latest")

    def test_uninstalled_model_raises(self):
        models = ["llama3.2:latest"]
        with self.assertRaises(assistant_main.OllamaError):
            assistant_main.choose_model(models, "nonexistent")


if __name__ == "__main__":
    unittest.main()
