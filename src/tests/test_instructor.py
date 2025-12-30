import pytest

from src.classes.instructor import Instructor


def test_instructor_create_ok():
    instructor = Instructor(full_name="Петро Петров", specialization="Програмування")
    info = instructor.get_instructor_info()
    assert "Петро Петров" in info
    assert "Програмування" in info


@pytest.mark.parametrize(
    "name,spec",
    [
        ("", "Програмування"),
        ("   ", "Програмування"),
        ("Петро", ""),
        ("Петро", "   "),
    ],
)
def test_instructor_validation_raises(name, spec):
    with pytest.raises(ValueError):
        Instructor(full_name=name, specialization=spec)
