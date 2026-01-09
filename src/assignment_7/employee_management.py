"""Function for managing the employees."""

import logging
from pathlib import Path

from src.assignment_7.employee import Employee
from src.assignment_7.employee_position import Developer, Intern, Manager

CSV_FORMAT_INFO = (
    "\nEnter the employee data as comma-separated values in the format:\n"
    "Employee ID,Name,Position,salary"
)

DATE_WORKDAY_RESULT = "{} is a weekday: {}"
DEVELOPER_MENTEES_HEADER = "Mentees of {}:"
DEVELOPER_NO_MENTEES = "{} has no mentees."

DISPLAY_MENU = """Employee details.
    1. To display details of all employees.
    2. To display details of Developers.
    3. To display details of Interns."""

EMPLOYEE_ALREADY_EXISTS = "Employee already exist."
EMPLOYEE_CREATED = "Employee created successfully."
EMPLOYEE_CREATED_SUCCESS = "Employee created successfully."
EMPLOYEE_ID_NOT_FOUND = "Employee ID doesn't exist."
EMPLOYEE_NAME_EMPTY = "Employee name can not be empty."
EMPLOYEE_POSITION_EMPTY = "Employee position cannot be empty."
ENTER_DATE = "\nEnter the date in YYYY-MM-DD format to check weekday: "
ENTER_DEVELOPER_ID = "Enter developer ID: "
ENTER_DISPLAY_CHOICE = "Enter your choice."
ENTER_EMPLOYEE_ID_CREATE = "\nEnter the employee ID: "
ENTER_EMPLOYEE_ID_EDIT = "\nEnter the employee ID to edit the salary: "
ENTER_EMPLOYEE_NAME = "Enter the name of the employee: "
ENTER_EMPLOYEE_POSITION = "Enter the position of the employee: "
ENTER_EMPLOYEE_SALARY = "Enter the salary of the employee: "
ENTER_INTERN_ID = "Enter intern ID: "
ENTER_NEW_SALARY = "Enter the new salary: "
ID_SHOULD_BE_POSITIVE = "ID should be positive."
INVALID_DEVELOPER_ID = "Invalid developer ID."
INVALID_DISPLAY_CHOICE = "Enter a valid choice."
INVALID_EMPLOYEE_POSITION = "Invalid employee position: {}"
INVALID_EMPLOYEE_POSITION_INPUT = "Invalid position for the employee."
INVALID_GENERIC_INPUT = "Invalid input. {}"
INVALID_ID_SALARY = "Invalid ID or salary, ID and salary must be integer."
INVALID_INTERN_ID = "Invalid intern ID."
INVALID_STRING_FORMAT = "The input does not match the format mentioned."
INTERN_MENTOR_INFO = "{}'s mentor is {}."
INTERN_NO_MENTOR = "{} has no mentor assigned."

LOGGER = logging.getLogger(__name__)

MENTOR_ASSIGNED = "{} is now mentored by {}."
NEGATIVE_ID_ERROR = "ID can not be a negative number."
NEGATIVE_SALARY_ERROR = "Salary can not be a negative number."
SALARY_SHOULD_BE_POSITIVE = "Salary should be a positive number."
SALARY_UPDATED_SUCCESS = "Salary updated successfully."


def create_employee_from_string(str_input: str) -> Employee:
    """Create an employee instance from a CSV-formatted string.

    Parse the input string in the format
    ``employee_id(int),name,position,salary(int)``
    and return an Employee object based on the position.

    Args:
        str_input: CSV-formatted employee data.

    Raises:
        IndexError: If the input does not contain exactly four values.
        ValueError: If type conversion fails or the position is invalid.

    Returns:
        Employee instance corresponding to the given position.
    """
    data = str_input.split(",")

    try:
        employee_id = int(data[0])
        name = data[1]
        position = data[2].lower()
        salary = float(data[3])
    except ValueError:
        raise
    except IndexError:
        raise IndexError(INVALID_STRING_FORMAT)
    else:
        if position == "manager":
            return Manager(employee_id, name, salary)
        if position == "developer":
            return Developer(employee_id, name, salary)
        if position == "intern":
            return Intern(employee_id, name, salary)

        raise ValueError(INVALID_EMPLOYEE_POSITION.format(position))


def add_employee() -> None:
    """Add a new employee using interactive user input.

    Validate all inputs and create the employee if the data is valid.
    """
    try:
        employee_id = input(ENTER_EMPLOYEE_ID_CREATE)
        employee_name = input(ENTER_EMPLOYEE_NAME).strip()
        employee_position = input(ENTER_EMPLOYEE_POSITION).strip()
        employee_salary = input(ENTER_EMPLOYEE_SALARY)

        if int(employee_id) <= 0:
            LOGGER.warning(ID_SHOULD_BE_POSITIVE)
            return

        if int(employee_id) in Employee.employee_data:
            LOGGER.warning(EMPLOYEE_ALREADY_EXISTS)
            return

        if not employee_name:
            LOGGER.warning(EMPLOYEE_NAME_EMPTY)
            return

        if not employee_position:
            LOGGER.warning(EMPLOYEE_POSITION_EMPTY)
            return

        if employee_position.lower() not in ("developer", "manager", "intern"):
            LOGGER.warning(INVALID_EMPLOYEE_POSITION_INPUT)
            return

        create_employee_from_string(
            (",").join([employee_id, employee_name, employee_position, employee_salary])
        )

    except ValueError as e:
        LOGGER.error(INVALID_GENERIC_INPUT.format(e))


def add_employee_from_csv_string() -> None:
    """Add a new employee using CSV-formatted input."""
    LOGGER.info(CSV_FORMAT_INFO)
    instance_str = input("Input: ").strip()
    new_emp = create_employee_from_string(instance_str)
    if new_emp:
        LOGGER.info(EMPLOYEE_CREATED)


def update_employee_salary() -> None:
    """Update the salary of an existing employee."""
    try:
        employee_id = int(input(ENTER_EMPLOYEE_ID_EDIT))
        new_salary = float(input(ENTER_NEW_SALARY))
    except ValueError:
        raise ValueError(INVALID_ID_SALARY)

    if employee_id <= 0:
        LOGGER.warning(NEGATIVE_ID_ERROR)
        return

    if new_salary <= 0:
        LOGGER.warning(INVALID_ID_SALARY)
        return

    if employee_id not in Employee.employee_data:
        LOGGER.warning(EMPLOYEE_ID_NOT_FOUND)
        return

    try:
        Employee.employee_data[employee_id].salary = new_salary
    except ValueError:
        LOGGER.warning(INVALID_ID_SALARY)
        return

    LOGGER.info(SALARY_UPDATED_SUCCESS)


def display_all_employee() -> None:
    """Display employees based on user-selected criteria."""
    try:
        print(DISPLAY_MENU)
        display_choice = int(input(ENTER_DISPLAY_CHOICE))
        if display_choice not in range(1, 4):
            raise ValueError
    except ValueError:
        raise ValueError(INVALID_DISPLAY_CHOICE)
    else:
        if display_choice == 2:
            Manager.display_developers()
        elif display_choice == 3:
            Manager.display_interns()
        else:
            Manager.display_employee()


def get_weekday() -> None:
    """Determine whether a given date falls on a workday."""
    date = input(ENTER_DATE).strip()
    try:
        print(DATE_WORKDAY_RESULT.format(date, Employee.is_workday(date)))
    except ValueError as error:
        raise ValueError(str(error)) from error


def assign_mentor() -> None:
    """Assign a developer as mentor to an intern."""
    try:
        intern_id = int(input(ENTER_INTERN_ID))
        developer_id = int(input(ENTER_DEVELOPER_ID))

        intern = Employee.employee_data.get(intern_id)
        if not intern or not isinstance(intern, Intern):
            LOGGER.error(INVALID_INTERN_ID)
            return

        intern.assign_mentor(developer_id)
        LOGGER.info(
            MENTOR_ASSIGNED.format(
                intern.name,
                Employee.employee_data[developer_id].name,
            )
        )

    except ValueError as error:
        LOGGER.error(str(error))


def display_intern_mentor() -> None:
    """Display mentor of a given intern."""
    try:
        intern_id = int(input(ENTER_INTERN_ID))
        intern = Employee.employee_data.get(intern_id)

        if not intern or not isinstance(intern, Intern):
            LOGGER.error(INVALID_INTERN_ID)
            return

        mentor_name = intern.get_mentor_name()
        if mentor_name is None:
            print(INTERN_NO_MENTOR.format(intern.name))
        else:
            print(INTERN_MENTOR_INFO.format(intern.name, mentor_name))

    except ValueError:
        LOGGER.error(INVALID_GENERIC_INPUT)


def display_developer_mentees() -> None:
    """Display all mentees of a developer."""
    try:
        developer_id = int(input(ENTER_DEVELOPER_ID))
        developer = Employee.employee_data.get(developer_id)

        if not developer or not isinstance(developer, Developer):
            LOGGER.error(INVALID_DEVELOPER_ID)
            return

        mentees = developer.get_mentees()
        if not mentees:
            print(DEVELOPER_NO_MENTEES.format(developer.name))
            return

        print(DEVELOPER_MENTEES_HEADER.format(developer.name))
        for mentee in mentees:
            print(mentee)

    except ValueError:
        LOGGER.error(INVALID_GENERIC_INPUT)


def initialise_logger(path: Path) -> None:
    """Configure and initialize the application logger.

    Set up console and file handlers with appropriate log levels
    and formatting.
    """
    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    if not root_logger.handlers:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(path, mode="a")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        root_logger.addHandler(stream_handler)
        root_logger.addHandler(file_handler)
