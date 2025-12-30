import pytest

from src.classes.student import Student


@pytest.mark.parametrize(
    "email",
    ["ivan@example.com", "test.user@mail.com", "a@b.co"],
)
def test_student_create_ok_valid_emails(email):
    student = Student(full_name="Іван Іванов", email=email)
    info = student.get_student_info()
    assert "Іван Іванов" in info
    assert email in info


@pytest.mark.parametrize("bad_email", ["", "   ", "ivanexample.com", "ivan@", "@example.com", "ivan@com"])
def test_student_invalid_email_raises(bad_email):
    with pytest.raises(ValueError):
        Student(full_name="Іван", email=bad_email)


@pytest.mark.parametrize("bad_name", ["", "   "])
def test_student_invalid_name_raises(bad_name):
    with pytest.raises(ValueError):
        Student(full_name=bad_name, email="ivan@example.com")


def test_student_enroll_course_adds_once_and_strips():
    student = Student(full_name="Іван Іванов", email="ivan@example.com")

    student.enroll_course("  Основи Python  ")
    student.enroll_course("Основи Python")  # дубль
    assert student.courses == ["Основи Python"]


def test_student_enroll_course_keeps_order():
    student = Student(full_name="Іван Іванов", email="ivan@example.com")

    student.enroll_course("Курс 1")
    student.enroll_course("Курс 2")
    student.enroll_course("Курс 1")  # дубль не додається

    assert student.courses == ["Курс 1", "Курс 2"]


def test_student_enroll_course_empty_raises():
    student = Student(full_name="Іван Іванов", email="ivan@example.com")
    with pytest.raises(ValueError):
        student.enroll_course("   ")
