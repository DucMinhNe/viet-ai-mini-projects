import importlib.util
import unittest
from pathlib import Path


MAIN_PATH = Path(__file__).resolve().parents[1] / "main.py"
spec = importlib.util.spec_from_file_location("invoice_main", MAIN_PATH)
invoice_main = importlib.util.module_from_spec(spec)
spec.loader.exec_module(invoice_main)


class ExtractFieldsTests(unittest.TestCase):
    def test_invoice_number_keeps_original_casing(self):
        text = (
            "Cong ty TNHH ABC\n"
            "Ma so thue: 0312345678\n"
            "So hoa don: HD-2026-0042\n"
            "Ngay: 15/04/2026\n"
            "Tong cong: 13.750.000 VND\n"
        )
        fields = invoice_main.extract_fields(text)
        self.assertEqual(fields["invoice_number"], "HD-2026-0042")

    def test_value_with_diacritics_is_preserved(self):
        text = "Công ty Sao Việt\nSố hóa đơn: SV-2026-A7\n"
        fields = invoice_main.extract_fields(text)
        self.assertEqual(fields["invoice_number"], "SV-2026-A7")


if __name__ == "__main__":
    unittest.main()
