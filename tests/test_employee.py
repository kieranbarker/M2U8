import pytest

from employee import Employee


def test_raise_salary():
    # Arrange
    fry_cook = Employee("SpongeBob", 30_000)

    # Act
    fry_cook.raise_salary(3.3)

    # Assert
    assert fry_cook.salary == pytest.approx(30_990)  # 30989.999999999996
