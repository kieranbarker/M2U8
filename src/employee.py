class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def raise_salary(self, by_percent: float) -> None:
        if by_percent <= 0:
            raise ValueError("Percentage must be positive")
        increase = self.salary * by_percent / 100
        self.salary += increase
