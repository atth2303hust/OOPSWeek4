# /****************/
# Họ và Tên: Phạm Anh Tú
# MSSV: 202419007
# /****************/

"""Lớp quản lý danh sách nhân sự của một kỳ lương."""

from typing import Optional

from employee import Employee


class Payroll:
    """Tổng hợp bảng lương bằng đa hình qua kiểu chung Employee."""

    def __init__(self, period: str) -> None:
        if period is None or not str(period).strip():
            raise ValueError("Kỳ lương không được rỗng.")
        self._period = str(period).strip()
        self._employees: list[Employee] = []

    @property
    def period(self) -> str:
        return self._period

    @property
    def employees(self) -> tuple[Employee, ...]:
        return tuple(self._employees)

    def addEmployee(self, employee: Employee) -> bool:
        if self.findEmployee(employee.employeeId) is not None:
            return False
        self._employees.append(employee)
        return True

    def findEmployee(self, employeeId: str) -> Optional[Employee]:
        for employee in self._employees:
            if employee.employeeId == employeeId:
                return employee
        return None

    def calculateTotalPayroll(self) -> float:
        # Gọi đa hình, không kiểm tra loại cụ thể bằng if/else.
        return sum(employee.calculateGrossPay() for employee in self._employees)

    def calculatePayrollByDepartment(self, department: str) -> float:
        return sum(
            employee.calculateGrossPay()
            for employee in self._employees
            if employee.department == department
        )

    def findHighestPaidEmployee(self) -> Optional[Employee]:
        if not self._employees:
            return None
        return max(self._employees, key=lambda employee: employee.calculateGrossPay())

    def displayPayroll(self) -> str:
        lines = [f"BẢNG LƯƠNG KỲ {self.period}", "=" * 90]
        if not self._employees:
            lines.append("Danh sách nhân sự đang rỗng.")
        else:
            # Lời gọi này được phân phối đa hình tới đúng lớp dẫn xuất.
            lines.extend(employee.displayPayrollInfo() for employee in self._employees)
            lines.append("-" * 90)
            lines.append(f"TỔNG BẢNG LƯƠNG: {self.calculateTotalPayroll():,.0f} VND")
        return "\n".join(lines)
