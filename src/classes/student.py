from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from src.interfaces.base import IStudent


@dataclass
class Student(IStudent):
    """Клас Student реалізує IStudent та описує студента."""

    full_name: str
    email: str
    courses: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.full_name.strip():
            raise ValueError("ПІБ студента не може бути порожнім.")
        if "@" not in self.email or not self.email.strip():
            raise ValueError("Некоректний email студента.")

    def get_student_info(self) -> str:
        return (
            f"Студент: {self.full_name}, "
            f"Email: {self.email}, "
            f"Курси: {self.courses}"
        )

    def enroll_course(self, course_name: str) -> None:
        course_name = course_name.strip()
        if not course_name:
            raise ValueError("Назва курсу не може бути порожньою.")
        if course_name not in self.courses:
            self.courses.append(course_name)
