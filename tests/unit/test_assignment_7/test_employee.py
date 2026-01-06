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


# is_workday() Tests - Edge Cases and Special Dates


def test_is_workday_leap_year_date():
    assert Employee.is_workday("2024-02-29") is True  # Thursday


def test_is_workday_with_leading_zeros():
    assert Employee.is_workday("2025-01-01") is True


def test_is_workday_new_year():
    assert Employee.is_workday("2025-01-01") is True  # Wednesday


def test_is_workday_end_of_year():
    assert Employee.is_workday("2025-12-31") is True  # Wednesday


# is_workday() Tests - Error Cases


def test_is_workday_invalid_format_raises_value_error():
    with pytest.raises(ValueError, match="Invalid date string."):
        Employee.is_workday("2025/12/29")


def test_is_workday_garbage_string_raises_value_error():
    with pytest.raises(ValueError):
        Employee.is_workday("not-a-date")


def test_is_workday_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        Employee.is_workday("")


def test_is_workday_invalid_month():
    with pytest.raises(ValueError):
        Employee.is_workday("2025-13-01")


def test_is_workday_invalid_day():
    with pytest.raises(ValueError):
        Employee.is_workday("2025-02-30")


def test_is_workday_missing_day():
    with pytest.raises(ValueError):
        Employee.is_workday("2025-12")


def test_is_workday_missing_month():
    with pytest.raises(ValueError):
        Employee.is_workday("2025")


def test_is_workday_wrong_separator():
    with pytest.raises(ValueError):
        Employee.is_workday("2025.12.29")


# Class Variable Behavior Tests


def test_employee_data_is_shared_across_instances():
    """Verify employee_data is a class variable, not instance variable."""
    emp1 = Employee(1, "Alice", "Developer", 50000)
    emp2 = Employee(2, "Bob", "Manager", 80000)

    assert emp1.employee_data is emp2.employee_data
    assert emp1.employee_data is Employee.employee_data


def test_employee_data_modification_affects_all_instances():
    emp1 = Employee(1, "Alice", "Developer", 50000)
    emp2 = Employee(2, "Bob", "Manager", 80000)

    # Access through any instance or class should show the same data
    assert len(emp1.employee_data) == 2
    assert len(emp2.employee_data) == 2
    assert len(Employee.employee_data) == 2


# Type Testing


def test_employee_id_type():
    emp = Employee(1, "Alice", "Developer", 50000)
    assert isinstance(emp.employee_id, int)


def test_employee_name_type():
    emp = Employee(1, "Alice", "Developer", 50000)
    assert isinstance(emp.name, str)


def test_employee_position_type():
    emp = Employee(1, "Alice", "Developer", 50000)
    assert isinstance(emp.position, str)


# Attribute Access Tests


def test_employee_attributes_are_accessible():
    emp = Employee(1, "Alice", "Developer", 50000)

    assert emp.employee_id == 1
    assert emp.name == "Alice"
    assert emp.position == "Developer"
    assert emp.salary == 50000


def test_employee_attributes_can_be_modified():
    emp = Employee(1, "Alice", "Developer", 50000)

    emp.name = "Alice Smith"
    emp.position = "Senior Developer"

    assert emp.name == "Alice Smith"
    assert emp.position == "Senior Developer"


# Integration Tests


def test_create_multiple_employees_and_display(capsys):
    Employee(1, "Alice", "Developer", 50000)
    Employee(2, "Bob", "Manager", 80000)
    Employee(3, "Charlie", "Intern", 15000)

    assert Employee.number_of_employees() == 3

    Employee.display_employee()
    captured = capsys.readouterr()

    assert "Alice" in captured.out
    assert "Bob" in captured.out
    assert "Charlie" in captured.out


def test_update_salary_multiple_times():
    emp = Employee(1, "Alice", "Developer", 50000)

    emp.salary = 55000
    assert emp.salary == 55000

    emp.salary = 60000
    assert emp.salary == 60000

    emp.salary = 65000
    assert emp.salary == 65000


def test_employee_registry_consistency():
    """Ensure that employee_data registry is always consistent."""
    emp1 = Employee(1, "Alice", "Developer", 50000)
    emp2 = Employee(2, "Bob", "Manager", 80000)

    # Check registry
    assert 1 in Employee.employee_data
    assert 2 in Employee.employee_data
    assert Employee.employee_data[1] is emp1
    assert Employee.employee_data[2] is emp2

    # Update salary through property
    emp1.salary = 60000

    # Verify the change is reflected in the registry
    assert Employee.employee_data[1].salary == 60000
