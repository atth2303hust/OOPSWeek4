# /****************/
# Họ và Tên: Phạm Anh Tú
# MSSV: 202419007
# /****************/

"""Nhân viên kinh doanh hưởng lương cơ bản và hoa hồng."""

from employee import Employee


class SalesEmployee(Employee):
    """Nhân viên kinh doanh có lương cơ bản, doanh số và tỷ lệ hoa hồng."""

    MAX_COMMISSION_RATE = 0.3

    def __init__(
        self,
        employeeId: str,
        fullName: str,
        baseSalary: float = 0.0,
        salesRevenue: float = 0.0,
        commissionRate: float = 0.0,
        department: str = Employee.DEFAULT_DEPARTMENT,
    ) -> None:
        super().__init__(employeeId, fullName, department)
        self._baseSalary = self._validate_non_negative(baseSalary, "Lương cơ bản")
        self._salesRevenue = self._validate_non_negative(salesRevenue, "Doanh số")
        self._commissionRate = self._validate_commission_rate(commissionRate)

    @staticmethod
    def _validate_non_negative(value: float, fieldName: str) -> float:
        number = float(value)
        if number < 0:
            raise ValueError(f"{fieldName} không được âm.")
        return number

    @classmethod
    def _validate_commission_rate(cls, value: float) -> float:
        number = float(value)
        if not 0 <= number <= cls.MAX_COMMISSION_RATE:
            raise ValueError("Tỷ lệ hoa hồng phải nằm trong khoảng từ 0 đến 0.3.")
        return number

    @property
    def baseSalary(self) -> float:
        return self._baseSalary

    @property
    def salesRevenue(self) -> float:
        return self._salesRevenue

    @property
    def commissionRate(self) -> float:
        return self._commissionRate

    def updateSalesRevenue(self, newRevenue: float) -> None:
        """Cập nhật doanh số có kiểm soát thay vì cho sửa thuộc tính trực tiếp."""
        self._salesRevenue = self._validate_non_negative(newRevenue, "Doanh số")

    def calculateGrossPay(self) -> float:
        return self.baseSalary + self.salesRevenue * self.commissionRate + self.monthlyBonus

    def getEmployeeType(self) -> str:
        return "SalesEmployee"

    def displayPayrollInfo(self) -> str:
        return (
            f"[{self.getEmployeeType()}] {self.employeeId} - {self.fullName} | "
            f"Phòng: {self.department} | Lương cơ bản: {self.baseSalary:,.0f} | "
            f"Doanh số: {self.salesRevenue:,.0f} | Hoa hồng: {self.commissionRate:.1%} | "
            f"Thưởng: {self.monthlyBonus:,.0f} | Gross pay: {self.calculateGrossPay():,.0f}"
        )
