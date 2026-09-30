# /****************/
# Mã sinh viên: <MSSV>
# Họ tên: <HỌ VÀ TÊN>
# /****************/

"""Lớp cơ sở cho hệ thống tính lương và thưởng nhân sự."""

from abc import ABC, abstractmethod
from typing import List

from bonus_record import BonusRecord


class Employee(ABC):
    """Lớp cơ sở trừu tượng chứa dữ liệu và hành vi chung của nhân sự."""

    DEFAULT_DEPARTMENT = "Unassigned"

    def __init__(
        self,
        employeeId: str,
        fullName: str,
        department: str = DEFAULT_DEPARTMENT,
    ) -> None:
        # Kiểm tra bất biến ngay khi đối tượng được tạo để tránh trạng thái sai.
        self._employeeId = self._validate_non_empty(employeeId, "Mã nhân sự")
        self._fullName = self._validate_non_empty(fullName, "Họ tên")
        self._department = self._validate_non_empty(department, "Phòng ban")
        self._monthlyBonus = 0.0
        self._bonusHistory: List[BonusRecord] = []

    @staticmethod
    def _validate_non_empty(value: str, fieldName: str) -> str:
        if value is None or not str(value).strip():
            raise ValueError(f"{fieldName} không được rỗng.")
        return str(value).strip()

    @property
    def employeeId(self) -> str:
        return self._employeeId

    @property
    def fullName(self) -> str:
        return self._fullName

    @property
    def department(self) -> str:
        return self._department

    @property
    def monthlyBonus(self) -> float:
        return self._monthlyBonus

    @property
    def bonusHistory(self) -> tuple[BonusRecord, ...]:
        # Trả tuple để bên ngoài không thể sửa trực tiếp danh sách nội bộ.
        return tuple(self._bonusHistory)

    def addBonus(self, *args) -> float:
        """Mô phỏng ba phiên bản addBonus() của đề trong Python.

        Hợp lệ:
        - addBonus(amount)
        - addBonus(amount, reason)
        - addBonus(rate, referenceAmount, reason)

        Python không nạp chồng theo chữ ký ở thời điểm biên dịch, vì vậy phương
        thức này phân phối lời gọi ở thời điểm chạy dựa trên số lượng đối số.
        """
        if len(args) == 1:
            amount = self._validate_positive(args[0], "Tiền thưởng")
            reason = "Thưởng cố định"
        elif len(args) == 2:
            amount = self._validate_positive(args[0], "Tiền thưởng")
            reason = self._validate_non_empty(args[1], "Lý do thưởng")
        elif len(args) == 3:
            rate = float(args[0])
            referenceAmount = self._validate_positive(args[1], "Giá trị tham chiếu")
            reason = self._validate_non_empty(args[2], "Lý do thưởng")
            if not 0 < rate <= 0.5:
                raise ValueError("Tỷ lệ thưởng phải lớn hơn 0 và không quá 0.5.")
            amount = rate * referenceAmount
        else:
            raise TypeError(
                "addBonus() chỉ chấp nhận 1, 2 hoặc 3 đối số theo đặc tả bài tập."
            )

        self._monthlyBonus += amount
        self._bonusHistory.append(BonusRecord(amount, reason))
        return amount

    @staticmethod
    def _validate_positive(value: float, fieldName: str) -> float:
        number = float(value)
        if number <= 0:
            raise ValueError(f"{fieldName} phải lớn hơn 0.")
        return number

    def resetBonus(self) -> None:
        """Đặt lại thưởng khi bắt đầu kỳ lương mới."""
        self._monthlyBonus = 0.0
        self._bonusHistory.clear()

    @abstractmethod
    def calculateGrossPay(self) -> float:
        """Tính tổng thu nhập trước khấu trừ."""
        raise NotImplementedError

    @abstractmethod
    def getEmployeeType(self) -> str:
        """Trả về tên loại nhân sự."""
        raise NotImplementedError

    def displayPayrollInfo(self) -> str:
        """Tạo chuỗi hiển thị chung; lớp dẫn xuất có thể ghi đè nếu cần."""
        return (
            f"[{self.getEmployeeType()}] {self.employeeId} - {self.fullName} | "
            f"Phòng: {self.department} | Thưởng: {self.monthlyBonus:,.0f} | "
            f"Gross pay: {self.calculateGrossPay():,.0f}"
        )
