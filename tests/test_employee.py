import pytest

from employee import Employee


def test_raise_salary():
    # Arrange
    fry_cook = Employee("SpongeBob", 30_000)

    # Act
    fry_cook.raise_salary(3.3)

    # Assert
    assert fry_cook.salary == 30_990


def test_raise_salary_rejects_zero():
    # Arrange
    cashier = Employee("Squidward", 35_000)

    # Act
    with pytest.raises(ValueError):
        cashier.raise_salary(0)

    # Assert
    assert cashier.salary == 35_000


def test_raise_salary_rejects_negative():
    # Arrange
    cashier = Employee("Squidward", 35_000)

    # Act
    with pytest.raises(ValueError):
        cashier.raise_salary(-5)

    # Assert
    assert cashier.salary == 35_000
