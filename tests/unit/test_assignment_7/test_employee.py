import pytest
from src.assignment_7.employee import Employee


@pytest.fixture(autouse=True)
def reset_employee_data():
    """Ensure Employee.employee_data is reset before and after every test.

    This is REQUIRED because employee_data is a global class-level registry.
    """
    Employee.employee_data.clear()
    yield
    Employee.employee_data.clear()


# Employee Creation and Registration Tests


def test_employee_creation_registers_employee():
    emp = Employee(1, "Alice", "Developer", 50000)

    assert Employee.number_of_employees() == 1
    assert Employee.employee_data[1] is emp


def test_multiple_employees_are_registered():
    Employee(1, "Alice", "Developer", 50000)
    Employee(2, "Bob", "Manager", 80000)

    assert Employee.number_of_employees() == 2
    assert set(Employee.employee_data.keys()) == {1, 2}


def test_employee_overwrites_same_id():
    Employee(1, "Alice", "Developer", 50000)
    emp2 = Employee(1, "Bob", "Manager", 80000)

    assert Employee.number_of_employees() == 1
    assert Employee.employee_data[1] is emp2
    assert Employee.employee_data[1].name == "Bob"


def test_employee_with_negative_id():
    emp = Employee(-1, "Alice", "Developer", 50000)
    assert emp.employee_id == -1


def test_employee_with_zero_id():
    emp = Employee(0, "Alice", "Developer", 50000)
    assert emp.employee_id == 0


# Salary Property Tests


def test_salary_getter_returns_correct_value():
    emp = Employee(1, "Alice", "Developer", 50000)

    assert emp.salary == 50000


def test_salary_setter_updates_salary():
    emp = Employee(1, "Alice", "Developer", 50000)

    emp.salary = 60000
    assert emp.salary == 60000


def test_salary_accepts_float_values():
    emp = Employee(1, "Alice", "Developer", 50000.75)

    assert emp.salary == 50000.75


def test_salary_is_private_attribute():
    emp = Employee(1, "Alice", "Developer", 50000)
    # Verify it's stored as private (name mangled)
    assert hasattr(emp, "_Employee__salary")
    assert emp._Employee__salary == 50000  # type: ignore


def test_salary_property_returns_float():
    emp = Employee(1, "Alice", "Developer", 50000)
    assert isinstance(emp.salary, (int, float))


# String Representation Tests


def test_employee_string_representation():
    emp = Employee(1, "Alice", "Developer", 50000)

    result = str(emp)

    assert "Employee Id: 1" in result
    assert "Name: Alice" in result
    assert "Position: Developer" in result
    assert "Salary: 50000" in result


def test_employee_string_representation_with_float_salary():
    emp = Employee(1, "Alice", "Developer", 50000.50)

    result = str(emp)

    assert "Employee Id: 1" in result
    assert "Name: Alice" in result
    assert "Position: Developer" in result
    assert "Salary: 50000.5" in result


# number_of_employees() Tests


def test_number_of_employees_empty():
    assert Employee.number_of_employees() == 0


def test_number_of_employees_non_empty():
    Employee(1, "Alice", "Developer", 50000)
    Employee(2, "Bob", "Intern", 15000)

    assert Employee.number_of_employees() == 2


def test_number_of_employees_after_overwrite():
    Employee(1, "Alice", "Developer", 50000)
    Employee(1, "Bob", "Manager", 80000)

    assert Employee.number_of_employees() == 1


# display_employee() Tests


def test_display_employee_when_empty(capsys):
    Employee.display_employee()
    captured = capsys.readouterr()

    assert "No employee exists in the database." in captured.out


def test_display_employee_with_employees(capsys):
    Employee(1, "Alice", "Developer", 50000)
    Employee(2, "Bob", "Manager", 80000)

    Employee.display_employee()
    captured = capsys.readouterr()

    assert "Alice" in captured.out
    assert "Bob" in captured.out
    assert "Developer" in captured.out
    assert "Manager" in captured.out


def test_display_employee_correct_format(capsys):
    Employee(1, "Alice", "Developer", 50000)
    Employee(2, "Bob", "Manager", 80000)

    Employee.display_employee()
    captured = capsys.readouterr()

    # Verify each employee is printed separately (no interleaving)
    assert captured.out.count("Employee Id:") == 2
    assert captured.out.count("Name:") == 2
    assert captured.out.count("Position:") == 2
    assert captured.out.count("Salary:") == 2


def test_display_employee_single_employee(capsys):
    Employee(1, "Alice", "Developer", 50000)

    Employee.display_employee()
    captured = capsys.readouterr()

    assert "Employee Id: 1" in captured.out
    assert "Alice" in captured.out


# is_workday() Tests - Weekdays


@pytest.mark.parametrize(
    "date_string",
    [
        "2025-12-29",  # Monday
        "2025-12-30",  # Tuesday
        "2025-12-31",  # Wednesday
        "2026-01-01",  # Thursday
        "2026-01-02",  # Friday
    ],
)
def test_is_workday_returns_true_for_weekdays(date_string):
    assert Employee.is_workday(date_string) is True


@pytest.mark.parametrize(
    "date_string",
    [
        "2025-12-27",  # Saturday
        "2025-12-28",  # Sunday
    ],
)
def test_is_workday_returns_false_for_weekends(date_string):
    assert Employee.is_workday(date_string) is False


# is_workday() Tests - Error Cases


@pytest.mark.parametrize(
    "date_string",
    [
        "not-a-date",
        "2025-13-01",
        "2025-02-30",
        "2025-12",
        "2025",
        "2025.12.29",
        "2025/12/29",
    ],
)
def test_is_workday_invalid_string_raises_value_error(date_string):
    with pytest.raises(ValueError):
        Employee.is_workday(date_string)
