from __future__ import annotations


class CourseRepository:
    """Репозиторій курсів (імітація джерела даних)."""

    def get_course_status(self, course_name: str) -> str:
        """Повертає статус курсу за назвою."""
        normalized = course_name.strip().lower()
        if normalized == "основи python":
            return "Active"
        return "Archived"
