# /****************/
# Mã sinh viên: <MSSV>
# Họ tên: <HỌ VÀ TÊN>
# /****************/

"""Nhân viên hưởng lương theo giờ."""

from employee import Employee


class HourlyEmployee(Employee):
    """Nhân viên được trả theo đơn giá giờ và số giờ làm trong tháng."""

    OVERTIME_THRESHOLD = 160.0
    MAX_WORKED_HOURS = 250.0
    OVERTIME_MULTIPLIER = 1.5

    def __init__(
        self,
        employeeId: str,
        fullName: str,
        hourlyRate: float = 0.0,
        workedHours: float = 0.0,
        department: str = Employee.DEFAULT_DEPARTMENT,
    ) -> None:
        super().__init__(employeeId, fullName, department)
        self._hourlyRate = self._validate_non_negative(hourlyRate, "Đơn giá giờ")
        self._workedHours = self._validate_worked_hours(workedHours)

    @staticmethod
    def _validate_non_negative(value: float, fieldName: str) -> float:
        number = float(value)
        if number < 0:
            raise ValueError(f"{fieldName} không được âm.")
        return number

    @classmethod
    def _validate_worked_hours(cls, value: float) -> float:
        number = float(value)
        if not 0 <= number <= cls.MAX_WORKED_HOURS:
            raise ValueError("Số giờ làm phải nằm trong khoảng từ 0 đến 250.")
        return number

    @property
    def hourlyRate(self) -> float:
        return self._hourlyRate

    @property
    def workedHours(self) -> float:
        return self._workedHours

    def calculateBasePay(self) -> float:
        regularHours = min(self.workedHours, self.OVERTIME_THRESHOLD)
        overtimeHours = max(0.0, self.workedHours - self.OVERTIME_THRESHOLD)
        return (
            regularHours * self.hourlyRate
            + overtimeHours * self.hourlyRate * self.OVERTIME_MULTIPLIER
        )

    def calculateGrossPay(self) -> float:
        return self.calculateBasePay() + self.monthlyBonus

    def getEmployeeType(self) -> str:
        return "HourlyEmployee"

    def displayPayrollInfo(self) -> str:
        return (
            f"[{self.getEmployeeType()}] {self.employeeId} - {self.fullName} | "
            f"Phòng: {self.department} | Đơn giá: {self.hourlyRate:,.0f} | "
            f"Giờ làm: {self.workedHours:g} | Thưởng: {self.monthlyBonus:,.0f} | "
            f"Gross pay: {self.calculateGrossPay():,.0f}"
        )
