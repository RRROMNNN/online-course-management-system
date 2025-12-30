import pytest

from src.classes.student import Student


def test_student_create_ok():
    student = Student(full_name="Іван Іванов", email="ivan@example.com")
    info = student.get_student_info()
    assert "Іван Іванов" in info
    assert "ivan@example.com" in info


@pytest.mark.parametrize("bad_email", ["", "   ", "ivanexample.com", "ivan@"])
def test_student_invalid_email_raises(bad_email):
    with pytest.raises(ValueError):
        Student(full_name="Іван", email=bad_email)


@pytest.mark.parametrize("bad_name", ["", "   "])
def test_student_invalid_name_raises(bad_name):
    with pytest.raises(ValueError):
        Student(full_name=bad_name, email="ivan@example.com")


def test_student_enroll_course_adds_once():
    student = Student(full_name="Іван Іванов", email="ivan@example.com")
    student.enroll_course("Основи Python")
    student.enroll_course("Основи Python")
    assert student.courses == ["Основи Python"]


def test_student_enroll_course_empty_raises():
    student = Student(full_name="Іван Іванов", email="ivan@example.com")
    with pytest.raises(ValueError):
        student.enroll_course("   ")
