from __future__ import annotations

from src.repository.course_repository import CourseRepository


class CourseService:
    """Сервіс курсів. Залежність передається через конструктор (Constructor Injection)."""

    def __init__(self, repository: CourseRepository) -> None:
        self._repository = repository

    def get_course_info(self, course_name: str) -> str:
        """Повертає інформацію про курс та його статус."""
        status = self._repository.get_course_status(course_name)
        return f"Курс: {course_name}, Статус: {status}"
