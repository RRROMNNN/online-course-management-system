from __future__ import annotations

from abc import ABC, abstractmethod


class ICourse(ABC):
    """Интерфейс учебного курса."""

    @abstractmethod
    def get_course_info(self) -> str:
        """Вернуть строку с информацией о курсе."""
        raise NotImplementedError

    @abstractmethod
    def get_status(self) -> str:
        """Вернуть текущий статус курса."""
        raise NotImplementedError

    @abstractmethod
    def update_status(self, new_status: str) -> None:
        """Обновить статус курса."""
        raise NotImplementedError


class IStudent(ABC):
    """Интерфейс студента."""

    @abstractmethod
    def get_student_info(self) -> str:
        """Вернуть строку с информацией о студенте."""
        raise NotImplementedError

    @abstractmethod
    def enroll_course(self, course_name: str) -> None:
        """Записать студента на курс."""
        raise NotImplementedError


class IInstructor(ABC):
    """Интерфейс преподавателя."""

    @abstractmethod
    def get_instructor_info(self) -> str:
        """Вернуть строку с информацией о преподавателе."""
        raise NotImplementedError
