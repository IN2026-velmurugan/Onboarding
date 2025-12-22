"""Script to run demonstrate the usage of employee module."""

import logging

from src.assignment_7.employee import (
    Employee,
    Manager,
    create_employee,
    create_employee_from_string,
    update_employee_salary,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)


def menu() -> None:
    """Displays the main menu options for the Employee Management System."""
    print("Employee management system")
    print("Menu")
    print("1. Add an employee.")
    print("2. Total number of employee.")
    print("3. Modify salary of an employee.")
    print("4. Display all employees.")
    print("5. Check weekday.")
    print("6. Create a instance using string data.")
    print("7. Exit.")


def display_menu() -> None:
    """Displays the Display menu options for the Employee Management System."""
    print("Employee details.")
    print("1. To display details of all employees.")
    print("2. To display details of Developers.")
    print("3. To display details of Interns.")


if __name__ == "__main__":
    while True:
        menu()
        try:
            choice: int = int(input("Enter your choice: "))

        except ValueError:
            logger.error("Invalid choice. Choice must be a number from 1 to 7.")
            continue
        if choice == 7:
            print("Exited successfully.")
            break

        elif choice == 1:
            try:
                employee_id: int = int(input("\nEnter the employee id: "))

                if employee_id <= 0:
                    print("Id can not be a negative number.")
                    continue

                if employee_id in Manager.employee_data:
                    print("Employee already exist.")
                    continue

                employee_name: str = input("Enter the name of the employee: ").strip()
                employee_position: str = input("Enter the position of the employee: ").strip()
                employee_salary: int = int(input("Enter the salary of the employee: "))
                if not employee_name:
                    print("Employee name can not be empty.")
                    continue

                if not employee_position:
                    print("Employee position cannot be empty.")
                    continue

                if employee_salary <= 0:
                    print("salary can not be a negative number.")
                    continue
                create_employee(employee_id, employee_name, employee_position, employee_salary)

            except ValueError:
                logger.error("Invalid id or salary. ID and salary must be integer.")
        elif choice == 2:
            print(f"Total number of employees: {Manager.number_of_employees()}")

        elif choice == 3:
            try:
                employee_id = int((input("\nEnter the employee id to edit the salary: ")))
                new_salary: int = int(input("Enter the new salary: "))
                if employee_id <= 0:
                    print("Id can not be a negative number.")
                    continue
                if new_salary <= 0:
                    print("Salary can not be a negative number.")
                    continue

            except ValueError:
                logger.error("Invalid id or salary, ID and salary must be integer.")

            else:
                update_employee_salary(employee_id, new_salary)

        elif choice == 4:
            try:
                display_menu()
                display_choice = int(input("Enter your choice."))
                if display_choice not in range(4):
                    raise ValueError("Invalid choice.")
            except ValueError:
                logger.error("Enter a valid choice.")
            else:
                if display_choice == 2:
                    Manager.display_developers()
                elif display_choice == 3:
                    Manager.display_interns()
                else:
                    Manager.display_employee()

        elif choice == 5:
            date: str = input("\nEnter the date in YYYY-MM-DD format to check weekday: ").strip()
            try:
                print(f"{date} is a weekday: {Employee.is_workday(date)}")
            except ValueError as error:
                logger.error(error)

        elif choice == 6:
            print("\nEnter the employee data as comma-separated values in the format:")
            print("Employee id,Name,Position,salary")
            instance_str: str = input("Input: ").strip()
            new_emp: Employee | None = create_employee_from_string(instance_str)

            if new_emp is not None:
                print("Employee created successfully.")

        else:
            print("Invalid choice. Choice must be number 1 to 7")
