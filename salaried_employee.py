# /****************/
# Mã sinh viên: <MSSV>
# Họ tên: <HỌ VÀ TÊN>
# /****************/

"""Nhân viên hưởng lương cố định."""

from employee import Employee


class SalariedEmployee(Employee):
    """Nhân viên có lương tháng cố định và phụ cấp trách nhiệm."""

    def __init__(
        self,
        employeeId: str,
        fullName: str,
        monthlySalary: float = 0.0,
        department: str = Employee.DEFAULT_DEPARTMENT,
        responsibilityAllowance: float = 0.0,
    ) -> None:
        super().__init__(employeeId, fullName, department)
        self._monthlySalary = self._validate_non_negative(monthlySalary, "Lương tháng")
        self._responsibilityAllowance = self._validate_non_negative(
            responsibilityAllowance, "Phụ cấp trách nhiệm"
        )

    @staticmethod
    def _validate_non_negative(value: float, fieldName: str) -> float:
        number = float(value)
        if number < 0:
            raise ValueError(f"{fieldName} không được âm.")
        return number

    @property
    def monthlySalary(self) -> float:
        return self._monthlySalary

    @property
    def responsibilityAllowance(self) -> float:
        return self._responsibilityAllowance

    def calculateGrossPay(self) -> float:
        return self.monthlySalary + self.responsibilityAllowance + self.monthlyBonus

    def getEmployeeType(self) -> str:
        return "SalariedEmployee"

    def displayPayrollInfo(self) -> str:
        return (
            f"[{self.getEmployeeType()}] {self.employeeId} - {self.fullName} | "
            f"Phòng: {self.department} | Lương tháng: {self.monthlySalary:,.0f} | "
            f"Phụ cấp: {self.responsibilityAllowance:,.0f} | "
            f"Thưởng: {self.monthlyBonus:,.0f} | Gross pay: {self.calculateGrossPay():,.0f}"
        )
