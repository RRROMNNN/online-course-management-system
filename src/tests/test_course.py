import pytest

from src.classes.course import Course


def test_course_create_ok():
    course = Course(
        name="Основи Python",
        description="Базові типи даних, функції та ООП",
        duration_hours=40,
        status="Active",
    )
    assert course.get_status() == "Active"
    assert "Курс: Основи Python" in course.get_course_info()


@pytest.mark.parametrize("bad_status", ["", "InProgress", "Done", "Архів"])
def test_course_invalid_status_raises(bad_status):
    with pytest.raises(ValueError):
        Course(
            name="Курс",
            description="Опис",
            duration_hours=10,
            status=bad_status,
        )


def test_course_update_status_ok():
    course = Course(name="Курс", description="Опис", duration_hours=10, status="Active")
    course.update_status("Completed")
    assert course.get_status() == "Completed"


def test_course_update_status_invalid_raises():
    course = Course(name="Курс", description="Опис", duration_hours=10, status="Active")
    with pytest.raises(ValueError):
        course.update_status("Unknown")


@pytest.mark.parametrize(
    "name,desc,duration",
    [
        ("", "Опис", 10),
        ("  ", "Опис", 10),
        ("Курс", "", 10),
        ("Курс", "   ", 10),
        ("Курс", "Опис", 0),
        ("Курс", "Опис", -5),
    ],
)
def test_course_validation_raises(name, desc, duration):
    with pytest.raises(ValueError):
        Course(name=name, description=desc, duration_hours=duration, status="Active")
