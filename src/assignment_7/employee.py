"""Module contains functions to manage employees."""

import datetime
from typing import Dict


class Employee:
    """Employee class is to manage employee data."""

    employee_data: Dict[int, "Employee"] = {}

    def __init__(self, employee_id: int, name: str, position: str, salary: int) -> None:
        """Initialize a new employee instance.

        Args:
            employee_id (int): A unique identifier for the employee.
            name (str): The full name of the employee.
            position (str): The job title of the employee.
            salary (int): The salary of the employee, stored as a private attribute


        Returns:
            None
        """
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.__salary = salary
        Employee.employee_data[self.employee_id] = self

    def __str__(self) -> str:
        """Provides a string representation of the employee details.

        Returns:
            str: A string containing the employee's name and position.
        """
        return (
            f"Employee Id: {self.employee_id}\n"
            f"Name: {self.name}\n"
            f"Position: {self.position}\n"
            f"Salary: {self.__salary}"
        )

    @property
    def salary(self) -> int:
        """Gets the salary of the employee.

        Returns:
            int: The salary of the employee.
        """
        return self.__salary

    @salary.setter
    def salary(self, salary) -> None:
        """Sets the salary of the employee.

        Args:
            salary (int): The new salary to be assigned to the employee.

        Returns:
            None.
        """
        self.__salary = salary

    @classmethod
    def number_of_employees(cls) -> int:
        """Provides the total number of employees in the company.

        Returns:
            int: Total number of employees in the database.
        """
        return len(cls.employee_data)

    @classmethod
    def display_employee(cls) -> None:
        """Displays all employee records currently stored in the database."""
        if not cls.number_of_employees():
            print("No employee exists in the database.")
            return

        for employee in cls.employee_data.values():
            print(employee)

    @staticmethod
    def is_workday(date: str) -> bool:
        """Determines if the given date is a workday.

        Args:
            date (str): Date in 'YYYY-MM-DD' format.

        Returns:
            bool: True if the date is a weekday, False otherwise.
        """
        try:
            week_day = datetime.datetime.strptime(date, "%Y-%m-%d").weekday()
        except ValueError:
            raise ValueError("Invalid date string.") from None
        else:
            return week_day not in (5, 6)


class Manager(Employee):
    """Manager is a subclass of Employee."""

    def __init__(self, manager_id: int, name: str, salary: int) -> None:
        """Initialize a new Manager instance.

        Args:
            manager_id (int): A unique identifier for the manager.
            name (str): The full name of the manager.
            salary (int): The salary of the manager, stored as a private attribute


        Returns:
            None
        """
        super().__init__(manager_id, name, "Manager", salary)

    @classmethod
    def display_developers(cls) -> None:
        """Prints all developer from the employee data."""
        developer_list: list[Developer] = [
            dev for _dev_id, dev in cls.employee_data.items() if isinstance(dev, Developer)
        ]

        if not developer_list:
            print("There are no developers in employee data.")
            return

        print("Developer list:")

        for dev in developer_list:
            print(dev.name)

    @classmethod
    def display_interns(cls) -> None:
        """Prints all interns in the employee data."""
        intern_list: list[Intern] = [
            intern for intern_id, intern in cls.employee_data.items() if isinstance(intern, Intern)
        ]

        if not intern_list:
            print("There are no interns in employee data.")
            return

        print("Intern list:")

        for intern in intern_list:
            print(intern.name)

    @classmethod
    def promote(cls, employee_id: int, new_role: str, increment_amount: int) -> None:
        """Promotes an employee to a new role by updating their position.

        Args:
            employee_id (int): The ID of the employee to be promoted.
            new_role (str): The new position/title for the employee.
            increment_amount (int): Increment amount of the employee.

        Returns:
            None
        """
        if employee_id not in cls.employee_data:
            print("Employee id doesn't exist.")
            return

        cls.employee_data[employee_id].position = new_role
        cls.employee_data[employee_id].salary += increment_amount
        print(f"{cls.employee_data[employee_id].name} is promoted to {new_role}.")


class Developer(Employee):
    """Developer is a subclass of Employee."""

    def __init__(self, developer_id: int, name: str, salary: int) -> None:
        """Initialize a new Developer instance.

        Args:
            developer_id (int): A unique identifier for the developer.
            name (str): The full name of the developer.
            salary (int): The salary of the developer, stored as a private attribute


        Returns:
            None
        """
        super().__init__(developer_id, name, "Developer", salary)

    @classmethod
    def number_of_developer(cls) -> None:
        """Counts and displays the number of Developer instances in the employee list.

        Returns:
            None
        """
        dev_count = 0
        for employee in cls.employee_data.values():
            if isinstance(employee, Developer):
                dev_count += 1
        print("The count of developers: ", dev_count)


class Intern(Employee):
    """Intern is a subclass of Employee."""

    def __init__(self, intern_id: int, name: str, salary: int) -> None:
        """Initialize a new Intern instance.

        Args:
            intern_id (int): A unique identifier for the intern.
            name (str): The full name of the intern.
            salary (int): The salary of the intern, stored as a private attribute


        Returns:
            None
        """
        super().__init__(intern_id, name, "Intern", salary)

    @classmethod
    def number_of_intern(cls) -> None:
        """Counts and displays the number of Intern instances in the employee list."""
        intern_count = 0
        for employee in cls.employee_data.values():
            if isinstance(employee, Intern):
                intern_count += 1
        print("The count of interns: ", intern_count)


def create_employee_from_string(str_input: str) -> Employee:
    """Creates a new employee from the string format "employee_id(int),name,position,salary(int)".

    Args:
        str_input: Input string in the mentioned format.

    Raises:
        IndexError: If the value provided is less than 4.
        ValueError: If the type conversion is failed.

    Returns:
        Employee instance based on the position.
    """
    data = str_input.split(",")
    try:
        employee_id = int(data[0])
        name = data[1]
        position = data[2]
        salary = int(data[3])
        position = position.lower()
    except ValueError:
        raise
    except IndexError:
        raise IndexError("The input does not match the format mentioned.")
    else:
        if position == "manager":
            return Manager(employee_id, name, salary)
        elif position == "developer":
            return Developer(employee_id, name, salary)
        elif position == "intern":
            return Intern(employee_id, name, salary)
        else:
            raise ValueError(f"Invalid employee position: {position}")


def create_employee(employee_id: int, employee_name, employee_position, employee_salary) -> None:
    """Creates a new employee if the employee  does not already exist.

    Args:
    employee_id (int): Id of the new employee.
    employee_name (str): Name of the new employee.
    employee_position: position of the new employee.
    employee_salary (int): Salary of the new employee.

    Returns:
        None.
    """
    Employee(employee_id, employee_name, employee_position, employee_salary)
    print("Employee created successfully.")


def update_employee_salary(employee_id: int, new_salary) -> None:
    """Update the employee salary based on the employee id.

    Args:
        employee_id (int): Id of the employee.
        new_salary (int): New salary of the employee.

    Returns:
        None.
    """
    if employee_id not in Employee.employee_data:
        print("Employee id doesn't exist.")
        return

    Employee.employee_data[employee_id].salary = new_salary
    print("Salary updated successfully.")
