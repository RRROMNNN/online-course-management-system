from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Set

from src.interfaces.base import ICourse


@dataclass
class Course(ICourse):
    """Класс Course реализует интерфейс ICourse и хранит информацию о курсе."""

    ALLOWED_STATUSES: ClassVar[Set[str]] = {"Active", "Completed", "Archived"}

    name: str
    description: str
    duration_hours: int
    status: str = "Active"

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Название курса не может быть пустым.")
        if not self.description.strip():
            raise ValueError("Описание курса не может быть пустым.")
        if self.duration_hours <= 0:
            raise ValueError("Длительность курса должна быть больше 0.")
        self._validate_status(self.status)

    def _validate_status(self, status: str) -> None:
        if status not in self.ALLOWED_STATUSES:
            raise ValueError(
                f"Некорректный статус: {status}. "
                f"Допустимые: {sorted(self.ALLOWED_STATUSES)}"
            )

    def get_course_info(self) -> str:
        return (
            f"Курс: {self.name}. "
            f"Описание: {self.description}. "
            f"Длительность: {self.duration_hours} ч."
        )

    def get_status(self) -> str:
        return self.status

    def update_status(self, new_status: str) -> None:
        self._validate_status(new_status)
        self.status = new_status
