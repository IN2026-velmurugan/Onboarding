"""Script to run demonstrate the usage of employee module."""

import logging
from pathlib import Path

from src.assignment_7.constants import (
    ENTER_CHOICE,
    EXIT_SUCCESS,
    INVALID_CHOICE_ERROR,
    TOTAL_EMPLOYEES,
)
from src.assignment_7.employee import Employee
from src.assignment_7.employee_manager import (
    add_employee,
    add_employee_from_csv_string,
    assign_mentor,
    display_all_employee,
    get_weekday,
    initialise_logger,
    menu,
    show_developer_mentees,
    show_intern_mentor,
    update_employee,
)

LOGGER = logging.getLogger(__name__)

if __name__ == "__main__":
    initialise_logger(Path("src/assignment_7/log.txt"))

    try:
        while True:
            menu()
            try:
                choice = int(input(ENTER_CHOICE))
            except ValueError:
                LOGGER.error(INVALID_CHOICE_ERROR)
                continue

            if choice == 0:
                LOGGER.info(EXIT_SUCCESS)
                break
            elif choice == 1:
                add_employee()
            elif choice == 2:
                LOGGER.info(TOTAL_EMPLOYEES.format(Employee.number_of_employees()))
            elif choice == 3:
                update_employee()
            elif choice == 4:
                display_all_employee()
            elif choice == 5:
                get_weekday()
            elif choice == 6:
                add_employee_from_csv_string()
            elif choice == 7:
                assign_mentor()
            elif choice == 8:
                show_intern_mentor()
            elif choice == 9:
                show_developer_mentees()
            else:
                LOGGER.error(INVALID_CHOICE_ERROR)

    except KeyboardInterrupt:
        LOGGER.info("Application interrupted by user.")
    except Exception:
        LOGGER.exception("Unexpected application error")
    finally:
        logging.shutdown()
