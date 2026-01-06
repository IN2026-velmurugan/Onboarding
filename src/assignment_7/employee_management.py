"""Function for managing the employees."""

import logging
from pathlib import Path

from src.assignment_7.constants import (
    CSV_FORMAT_INFO,
    DATE_WORKDAY_RESULT,
    DEVELOPER_MENTEES_HEADER,
    DEVELOPER_NO_MENTEES,
    DISPLAY_MENU,
    EMPLOYEE_ALREADY_EXISTS,
    EMPLOYEE_CREATED,
    EMPLOYEE_ID_NOT_FOUND,
    EMPLOYEE_NAME_EMPTY,
    EMPLOYEE_POSITION_EMPTY,
    ENTER_DATE,
    ENTER_DEVELOPER_ID,
    ENTER_DISPLAY_CHOICE,
    ENTER_EMPLOYEE_ID_CREATE,
    ENTER_EMPLOYEE_ID_EDIT,
    ENTER_EMPLOYEE_NAME,
    ENTER_EMPLOYEE_POSITION,
    ENTER_EMPLOYEE_SALARY,
    ENTER_INTERN_ID,
    ENTER_NEW_SALARY,
    ID_SHOULD_BE_POSITIVE,
    INTERN_MENTOR_INFO,
    INTERN_NO_MENTOR,
    INVALID_DEVELOPER_ID,
    INVALID_DISPLAY_CHOICE,
    INVALID_EMPLOYEE_POSITION,
    INVALID_EMPLOYEE_POSITION_INPUT,
    INVALID_GENERIC_INPUT,
    INVALID_ID_SALARY,
    INVALID_INTERN_ID,
    INVALID_STRING_FORMAT,
    MAIN_MENU,
    MENTOR_ASSIGNED,
    NEGATIVE_ID_ERROR,
    SALARY_UPDATED_SUCCESS,
)
from src.assignment_7.employee import Employee
from src.assignment_7.employee_position import Developer, Intern, Manager

LOGGER = logging.getLogger(__name__)


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


def menu() -> None:
    """Display the main menu of the Employee Management System."""
    print(MAIN_MENU)


def display_menu() -> None:
    """Display employee display options."""
    print(DISPLAY_MENU)


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
        display_menu()
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


def show_intern_mentor() -> None:
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


def show_developer_mentees() -> None:
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
