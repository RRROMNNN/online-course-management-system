import pytest

from src.services.course_service import CourseService
from src.repository.course_repository import CourseRepository


def test_course_service_with_real_repository():
    repo = CourseRepository()
    service = CourseService(repo)

    result = service.get_course_info("Основи Python")

    assert "Курс: Основи Python" in result
    assert "Статус: Active" in result


class FakeCourseRepository:
    """Підставний репозиторій для перевірки DI."""

    def __init__(self, status: str) -> None:
        self.status = status
        self.calls = 0
        self.last_course_name = None

    def get_course_status(self, course_name: str) -> str:
        self.calls += 1
        self.last_course_name = course_name
        return self.status


@pytest.mark.parametrize("status", ["Active", "Completed", "Archived"])
def test_course_service_uses_injected_repository(status):
    repo = FakeCourseRepository(status=status)
    service = CourseService(repo)

    result = service.get_course_info("Курс X")

    assert repo.calls == 1
    assert repo.last_course_name == "Курс X"
    assert f"Статус: {status}" in result
