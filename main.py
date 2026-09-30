# /****************/
# Họ và Tên: Phạm Anh Tú
# MSSV: 202419007
# /****************/

"""Chương trình minh họa theo đúng dữ liệu kiểm thử của đề Lab W04."""

from hourly_employee import HourlyEmployee
from payroll import Payroll
from salaried_employee import SalariedEmployee
from sales_employee import SalesEmployee


def formatMoney(value: float) -> str:
    """Định dạng số tiền theo kiểu phân tách hàng nghìn quen thuộc ở Việt Nam."""
    return f"{value:,.0f}".replace(",", ".") + " VND"


def createSamplePayroll() -> Payroll:
    payroll = Payroll("2026-09")

    # E001: lương cố định + phụ cấp + thưởng cố định.
    e001 = SalariedEmployee(
        "E001", "Nguyễn Minh An", 15_000_000, "Đào tạo", 2_000_000
    )
    e001.addBonus(1_000_000)

    # E002: 150 giờ, chưa chạm ngưỡng làm thêm.
    e002 = HourlyEmployee("E002", "Trần Thu Bình", 100_000, 150, "Hỗ trợ")
    e002.addBonus(500_000, "Thưởng hoàn thành công việc")

    # E003: 170 giờ, có 10 giờ tính hệ số 1.5.
    e003 = HourlyEmployee("E003", "Lê Hoàng Chi", 100_000, 170, "Hỗ trợ")

    # E004: lương cơ bản + hoa hồng + thưởng 2% của 50 triệu.
    e004 = SalesEmployee(
        "E004", "Phạm Quốc Dũng", 8_000_000, 200_000_000, 0.05, "Kinh doanh"
    )
    e004.addBonus(0.02, 50_000_000, "Thưởng theo tỷ lệ")

    for employee in (e001, e002, e003, e004):
        payroll.addEmployee(employee)

    return payroll


def runDemo() -> None:
    payroll = createSamplePayroll()
    print(payroll.displayPayroll())

    print("\nKIỂM TRA KẾT QUẢ MONG ĐỢI")
    print("-" * 90)
    expected = {
        "E001": 18_000_000,
        "E002": 15_500_000,
        "E003": 17_500_000,
        "E004": 19_000_000,
    }
    for employeeId, expectedPay in expected.items():
        employee = payroll.findEmployee(employeeId)
        actualPay = employee.calculateGrossPay() if employee else -1
        status = "PASS" if actualPay == expectedPay else "FAIL"
        print(
            f"{employeeId}: actual={formatMoney(actualPay):>18} | "
            f"expected={formatMoney(expectedPay):>18} | {status}"
        )

    total = payroll.calculateTotalPayroll()
    supportTotal = payroll.calculatePayrollByDepartment("Hỗ trợ")
    highest = payroll.findHighestPaidEmployee()
    print(f"\nTổng bảng lương: {formatMoney(total)} (mong đợi 70.000.000 VND)")
    print(f"Tổng phòng Hỗ trợ: {formatMoney(supportTotal)} (mong đợi 33.000.000 VND)")
    if highest:
        print(
            f"Nhân sự thu nhập cao nhất: {highest.employeeId} - {highest.fullName} "
            f"({formatMoney(highest.calculateGrossPay())})"
        )

    duplicate = payroll.addEmployee(
        SalariedEmployee("E001", "Nhân viên trùng mã", 1_000_000)
    )
    print(f"Thử thêm trùng mã E001: {'BỊ TỪ CHỐI - PASS' if not duplicate else 'FAIL'}")


if __name__ == "__main__":
    runDemo()
