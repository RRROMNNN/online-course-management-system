from __future__ import annotations

from dataclasses import dataclass

from src.interfaces.base import IInstructor


@dataclass
class Instructor(IInstructor):
    """Клас Instructor реалізує IInstructor та описує викладача."""

    full_name: str
    specialization: str

    def __post_init__(self) -> None:
        if not self.full_name.strip():
            raise ValueError("ПІБ викладача не може бути порожнім.")
        if not self.specialization.strip():
            raise ValueError("Спеціалізація не може бути порожньою.")

    def get_instructor_info(self) -> str:
        return (
            f"Викладач: {self.full_name}, "
            f"Спеціалізація: {self.specialization}"
        )
