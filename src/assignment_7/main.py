"""Script to demonstrate the usage of employee module."""

import logging
from pathlib import Path

from src.assignment_7.constants import (
    ENTER_CHOICE,
    ERROR_ATTEMPT_EXCEEDED,
    ERROR_INVALID_OPERATION,
    ERROR_UNEXPECTED,
    EXIT_SUCCESS,
    INFO_INTERRUPTED,
    INVALID_CHOICE_ERROR,
    TOTAL_EMPLOYEES,
)
from src.assignment_7.employee import Employee
from src.assignment_7.employee_management import (
    add_employee,
    add_employee_from_csv_string,
    assign_mentor,
    display_all_employee,
    get_weekday,
    initialise_logger,
    menu,
    show_developer_mentees,
    show_intern_mentor,
    update_employee_salary,
)

LOGGER = logging.getLogger(__name__)


def main() -> None:
    """Main function acting as start point."""
    try:
        choice = -1
        count = 0
        while choice != 0 and count < 5:
            menu()
            try:
                choice = int(input(ENTER_CHOICE))
            except ValueError:
                count += 1
                LOGGER.error(INVALID_CHOICE_ERROR)
                continue
            try:
                if choice == 0:
                    LOGGER.info(EXIT_SUCCESS)
                    break
                elif choice == 1:
                    add_employee()
                elif choice == 2:
                    print(TOTAL_EMPLOYEES.format(Employee.number_of_employees()))
                elif choice == 3:
                    update_employee_salary()
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
                    count += 1
                    LOGGER.error(INVALID_CHOICE_ERROR)
            except ValueError as e:
                LOGGER.error(ERROR_INVALID_OPERATION.format(e))
                continue
        else:
            if count == 5:
                raise ValueError(ERROR_ATTEMPT_EXCEEDED)

    except KeyboardInterrupt:
        LOGGER.info(INFO_INTERRUPTED)
    except ValueError as e:
        LOGGER.warning(e)
    except Exception:
        LOGGER.exception(ERROR_UNEXPECTED)
    finally:
        logging.shutdown()


if __name__ == "__main__":
    initialise_logger(Path("src/assignment_7/log.txt"))
    main()
