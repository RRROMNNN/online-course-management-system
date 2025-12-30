from __future__ import annotations

from abc import ABC, abstractmethod


class ICourse(ABC):
    """Інтерфейс навчального курсу."""

    @abstractmethod
    def get_course_info(self) -> str:
        """Повертає рядок з інформацією про навчальний курс."""
        raise NotImplementedError


    @abstractmethod
    def get_status(self) -> str:
        """Повертає поточний статус курсу."""
        raise NotImplementedError


    @abstractmethod
    def update_status(self, new_status: str) -> None:
        """Оновлює статус навчального курсу."""
        raise NotImplementedError


class IStudent(ABC):
    """Інтерфейс студента."""

    @abstractmethod
    def get_student_info(self) -> str:
        """Повертає рядок з інформацією про студента."""
        raise NotImplementedError


    @abstractmethod
    def enroll_course(self, course_name: str) -> None:
        """Реєструє студента на навчальний курс."""
        raise NotImplementedError


class IInstructor(ABC):
    """Інтерфейс викладача."""

    @abstractmethod
    def get_instructor_info(self) -> str:
        """Повертає рядок з інформацією про викладача."""
        raise NotImplementedError
