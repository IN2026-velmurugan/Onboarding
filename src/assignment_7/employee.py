"""Employee base class."""

import datetime


class Employee:
    """Manage employee data and operations."""

    employee_data: dict[int, "Employee"] = {}

    def __init__(self, employee_id: int, name: str, position: str, salary: float) -> None:
        """Initialize an employee instance.

        Args:
            employee_id: Unique identifier for the employee.
            name: Full name of the employee.
            position: Job title of the employee.
            salary: Salary assigned to the employee.

        Returns:
            None.
        """
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.__salary = salary
        Employee.employee_data[self.employee_id] = self

    def __str__(self) -> str:
        """Return a formatted string representation of the employee.

        Returns:
            String containing employee details.
        """
        return (
            f"Employee Id: {self.employee_id}\n"
            f"Name: {self.name}\n"
            f"Position: {self.position}\n"
            f"Salary: {self.__salary}"
        )

    @property
    def salary(self) -> float:
        """Return the employee salary.

        Returns:
            Employee salary value.
        """
        return self.__salary

    @salary.setter
    def salary(self, salary: float) -> None:
        """Update the employee salary.

        Args:
            salary: New salary value.

        Returns:
            None.
        """
        self.__salary = salary

    @classmethod
    def number_of_employees(cls) -> int:
        """Return the total number of employees.

        Returns:
            Number of employees stored in the registry.
        """
        return len(cls.employee_data)

    @classmethod
    def display_employee(cls) -> None:
        """Display all employees in the registry."""
        if not cls.number_of_employees():
            print("No employee exists in the database.")
            return

        for employee in cls.employee_data.values():
            print(employee)

    @staticmethod
    def is_workday(date: str) -> bool:
        """Determine whether a given date is a workday.

        Args:
            date: Date string in ``YYYY-MM-DD`` format.

        Returns:
            True if the date is a weekday, otherwise False.

        Raises:
            ValueError: If the date string format is invalid.
        """
        try:
            week_day = datetime.datetime.strptime(date, "%Y-%m-%d").weekday()
        except ValueError:
            raise ValueError("Invalid date string.") from None
        else:
            return week_day not in (5, 6)
