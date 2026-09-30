# /****************/
# Họ và Tên: Phạm Anh Tú
# MSSV: 202419007
# /****************/

"""Kiểm thử đơn vị cho hệ thống bảng lương Lab W04."""

import os
import sys
import unittest

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from hourly_employee import HourlyEmployee
from payroll import Payroll
from salaried_employee import SalariedEmployee
from sales_employee import SalesEmployee


class PayrollTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.payroll = Payroll("2026-09")
        self.e001 = SalariedEmployee(
            "E001", "Nguyễn Minh An", 15_000_000, "Đào tạo", 2_000_000
        )
        self.e001.addBonus(1_000_000)
        self.e002 = HourlyEmployee("E002", "Trần Thu Bình", 100_000, 150, "Hỗ trợ")
        self.e002.addBonus(500_000, "Thưởng cố định")
        self.e003 = HourlyEmployee("E003", "Lê Hoàng Chi", 100_000, 170, "Hỗ trợ")
        self.e004 = SalesEmployee(
            "E004", "Phạm Quốc Dũng", 8_000_000, 200_000_000, 0.05, "Kinh doanh"
        )
        self.e004.addBonus(0.02, 50_000_000, "Thưởng tỷ lệ")
        for employee in (self.e001, self.e002, self.e003, self.e004):
            self.payroll.addEmployee(employee)

    def test_01_salaried_expected_pay(self):
        self.assertEqual(self.e001.calculateGrossPay(), 18_000_000)

    def test_02_hourly_without_overtime(self):
        self.assertEqual(self.e002.calculateGrossPay(), 15_500_000)

    def test_03_hourly_with_overtime(self):
        self.assertEqual(self.e003.calculateGrossPay(), 17_500_000)

    def test_04_sales_expected_pay(self):
        self.assertEqual(self.e004.calculateGrossPay(), 19_000_000)

    def test_05_total_payroll(self):
        self.assertEqual(self.payroll.calculateTotalPayroll(), 70_000_000)

    def test_06_support_department_total(self):
        self.assertEqual(self.payroll.calculatePayrollByDepartment("Hỗ trợ"), 33_000_000)

    def test_07_highest_paid_employee(self):
        self.assertEqual(self.payroll.findHighestPaidEmployee().employeeId, "E004")

    def test_08_duplicate_employee_rejected(self):
        duplicate = SalariedEmployee("E001", "Duplicate", 1_000_000)
        self.assertFalse(self.payroll.addEmployee(duplicate))

    def test_09_invalid_worked_hours_above_250(self):
        with self.assertRaises(ValueError):
            HourlyEmployee("X001", "Sai giờ", 100_000, 251)

    def test_10_invalid_commission_rate(self):
        with self.assertRaises(ValueError):
            SalesEmployee("X002", "Sai hoa hồng", 1, 1, 0.31)

    def test_11_invalid_fixed_bonus(self):
        with self.assertRaises(ValueError):
            self.e001.addBonus(0)

    def test_12_invalid_bonus_rate(self):
        with self.assertRaises(ValueError):
            self.e001.addBonus(0.51, 1_000_000, "Sai tỷ lệ")

    def test_13_empty_bonus_reason(self):
        with self.assertRaises(ValueError):
            self.e001.addBonus(10_000, "   ")

    def test_14_empty_payroll_highest_is_none(self):
        self.assertIsNone(Payroll("2026-10").findHighestPaidEmployee())

    def test_15_reset_bonus(self):
        self.e001.resetBonus()
        self.assertEqual(self.e001.monthlyBonus, 0)
        self.assertEqual(len(self.e001.bonusHistory), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
