"""Script to demonstrate the usage of employee module."""

import logging
from pathlib import Path

from src.assignment_7.employee import Employee
from src.assignment_7.employee_management import (
    add_employee,
    add_employee_from_csv_string,
    assign_mentor,
    display_all_employee,
    display_developer_mentees,
    display_intern_mentor,
    get_weekday,
    initialise_logger,
    update_employee_salary,
)

ENTER_CHOICE = "Enter your choice between 0 and 9:"
ERROR_ATTEMPT_EXCEEDED = "Attempt exceeded. Please try again."
ERROR_INVALID_OPERATION = "Invalid operation : {}"
ERROR_UNEXPECTED = "Unexpected application error"
EXIT_SUCCESS = "Exited successfully."
INFO_INTERRUPTED = "Application interrupted by user."
INVALID_CHOICE_ERROR = "Invalid choice. Choice must be a number from 1 to 7."

LOGGER = logging.getLogger(__name__)

MAIN_MENU = """
Employee management system
    Menu
    1. Add an employee.
    2. Total number of employee.
    3. Modify salary of an employee.
    4. Display all employees.
    5. Check weekday.
    6. Create a instance using string data.
    7. Assign mentor
    8. Show intern mentor
    9. Show developer mentees
    0. Exit."""

MAX_ATTEMPTS = 5

TOTAL_EMPLOYEES = "Total number of employees: {}"

menu_actions = {
    1: add_employee,
    2: lambda: print(TOTAL_EMPLOYEES.format(Employee.number_of_employees())),
    3: update_employee_salary,
    4: display_all_employee,
    5: get_weekday,
    6: add_employee_from_csv_string,
    7: assign_mentor,
    8: display_intern_mentor,
    9: display_developer_mentees,
}


def start_employee_manager() -> None:
    """Start the employee manager console application."""
    choice = -1
    count = 0
    while choice != 0 and count < MAX_ATTEMPTS:
        print(MAIN_MENU)
        try:
            choice = int(input(ENTER_CHOICE))
        except ValueError:
            count += 1
            LOGGER.error(INVALID_CHOICE_ERROR)
            continue
        if choice == 0:
            LOGGER.info(EXIT_SUCCESS)
            return

        try:
            action = menu_actions.get(choice)
            if action is None:
                raise ValueError(INVALID_CHOICE_ERROR)
            action()
        except ValueError as e:
            count += 1
            LOGGER.error(ERROR_INVALID_OPERATION.format(e))
            continue
    else:
        if count == MAX_ATTEMPTS:
            raise ValueError(ERROR_ATTEMPT_EXCEEDED)


if __name__ == "__main__":
    initialise_logger(Path("logs_output/log.txt"))
    try:
        start_employee_manager()
    except KeyboardInterrupt:
        LOGGER.info(INFO_INTERRUPTED)
    except ValueError as e:
        LOGGER.warning(e)
    except Exception:
        LOGGER.exception(ERROR_UNEXPECTED)
    finally:
        logging.shutdown()
