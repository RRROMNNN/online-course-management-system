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

        email = self.email.strip()

        # Проста, але адекватна валідація:
        # - рівно один '@'
        # - є частина до '@' і після '@'
        # - у домені є крапка (example.com)
        if not email:
            raise ValueError("Некоректний email студента.")
        if email.count("@") != 1:
            raise ValueError("Некоректний email студента.")

        local_part, domain_part = email.split("@")
        if not local_part or not domain_part:
            raise ValueError("Некоректний email студента.")
        if "." not in domain_part or domain_part.startswith(".") or domain_part.endswith("."):
            raise ValueError("Некоректний email студента.")

        self.email = email

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
