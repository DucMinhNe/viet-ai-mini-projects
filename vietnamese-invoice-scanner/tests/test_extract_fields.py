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

    def test_branch_tax_code_with_hyphen_is_preserved(self):
        text = "Mã số thuế: 0101234567-001\nSố hóa đơn: HD-123\n"
        fields = invoice_main.extract_fields(text)
        self.assertEqual(fields["tax_code"], "0101234567-001")

    def test_zero_total_vnd_counted_in_confidence(self):
        text = (
            "Công ty TNHH Dịch vụ\n"
            "Mã số thuế: 0101234567\n"
            "Số hóa đơn: HD-001\n"
            "Ngày: 01/09/2026\n"
            "Tổng cộng: 0 VND\n"
        )
        fields = invoice_main.extract_fields(text)
        self.assertEqual(fields["total_vnd"], 0)
        self.assertEqual(fields["confidence"], 1.0)

    def test_statutory_date_vietnamese_format_is_preserved(self):
        text = (
            "Công ty Cổ phần Sao Kim\n"
            "Mã số thuế: 0312345678\n"
            "Số hóa đơn: HD-2026-9999\n"
            "Ngày 15 tháng 04 năm 2026\n"
            "Tổng tiền: 25.000.000 VND\n"
        )
        fields = invoice_main.extract_fields(text)
        self.assertEqual(fields["date"], "15 tháng 04 năm 2026")
        self.assertEqual(fields["total_vnd"], 25000000)

    def test_iso_date_format_and_thanh_tien_are_preserved(self):
        text = (
            "Công ty TNHH Logistics\n"
            "Mã số thuế: 0312345678\n"
            "Số hóa đơn: HD-2026-0001\n"
            "Date: 2026-04-15\n"
            "Thành tiền: 10.500.000 VND\n"
        )
        fields = invoice_main.extract_fields(text)
        self.assertEqual(fields["date"], "2026-04-15")
        self.assertEqual(fields["total_vnd"], 10500000)

    def test_extract_vendor_skips_accented_invoice_header_titles(self):
        text = (
            "HÓA ĐƠN GIÁ TRỊ GIA TĂNG\n"
            "(Bản thể hiện của hóa đơn điện tử)\n"
            "Công ty Cổ phần Công nghệ Minh Lê\n"
            "Mã số thuế: 0312345678\n"
            "Số hóa đơn: HD-2026-0042\n"
            "Ngày: 27/11/2026\n"
            "Tổng cộng: 1.000.000 VND\n"
        )
        fields = invoice_main.extract_fields(text)
        self.assertEqual(fields["vendor"], "Công ty Cổ phần Công nghệ Minh Lê")

    def test_dot_delimited_date_format_is_extracted(self):
        text = (
            "Công ty TNHH Dịch vụ Số\n"
            "Mã số thuế: 0312345678\n"
            "Số hóa đơn: HD-2026-0099\n"
            "Ngày: 27.11.2026\n"
            "Tổng cộng: 500.000 VND\n"
        )
        fields = invoice_main.extract_fields(text)
        self.assertEqual(fields["date"], "27.11.2026")


if __name__ == "__main__":
    unittest.main()
