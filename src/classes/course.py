from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Set

from src.interfaces.base import ICourse


@dataclass
class Course(ICourse):
    """Клас Course реалізує ICourse та зберігає інформацію про навчальний курс."""

    ALLOWED_STATUSES: ClassVar[Set[str]] = {"Active", "Completed", "Archived"}

    name: str
    description: str
    duration_hours: int
    status: str = "Active"

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Назва курсу не може бути порожньою.")
        if not self.description.strip():
            raise ValueError("Опис курсу не може бути порожнім.")
        if self.duration_hours <= 0:
            raise ValueError("Тривалість курсу повинна бути більшою за 0.")
        self._validate_status(self.status)

    def _validate_status(self, status: str) -> None:
        if status not in self.ALLOWED_STATUSES:
            raise ValueError(
                f"Некоректний статус: {status}. "
                f"Допустимі: {sorted(self.ALLOWED_STATUSES)}"
            )

    def get_course_info(self) -> str:
        return (
            f"Курс: {self.name}. "
            f"Опис: {self.description}. "
            f"Тривалість: {self.duration_hours} год."
        )

    def get_status(self) -> str:
        return self.status

    def update_status(self, new_status: str) -> None:
        self._validate_status(new_status)
        self.status = new_status
