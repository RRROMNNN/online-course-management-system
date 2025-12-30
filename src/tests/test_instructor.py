import pytest

from src.classes.instructor import Instructor


@pytest.mark.parametrize(
    "name,spec",
    [
        ("Петро Петров", "Програмування"),
        ("Ірина Іваненко", "Аналіз даних"),
        ("Олег Сидоренко", "Кібербезпека"),
    ],
)
def test_instructor_create_ok(name, spec):
    instructor = Instructor(full_name=name, specialization=spec)
    info = instructor.get_instructor_info()
    assert name in info
    assert spec in info


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
