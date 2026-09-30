# /****************/
# Mã sinh viên: <MSSV>
# Họ tên: <HỌ VÀ TÊN>
# /****************/

"""Cấu trúc dữ liệu lưu một lần ghi nhận thưởng."""

from dataclasses import dataclass


@dataclass(frozen=True)
class BonusRecord:
    """Biểu diễn một khoản thưởng đã được cộng cho nhân sự."""

    amount: float
    reason: str

    def __post_init__(self) -> None:
        if self.amount <= 0:
            raise ValueError("Tiền thưởng phải lớn hơn 0.")
        if not self.reason.strip():
            raise ValueError("Lý do thưởng không được rỗng.")
