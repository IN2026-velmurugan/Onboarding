import logging
from unittest.mock import patch

import pytest
from src.assignment_7 import constants
from src.assignment_7.employee import Employee
from src.assignment_7.employee_management import (
    add_employee,
    add_employee_from_csv_string,
    assign_mentor,
    create_employee_from_string,
    display_all_employee,
    display_menu,
    get_weekday,
    initialise_logger,
    menu,
    show_developer_mentees,
    show_intern_mentor,
    update_employee_salary,
)
from src.assignment_7.employee_position import Developer, Intern, Manager


@pytest.fixture(autouse=True)
def reset_employee_data():
    """Reset Employee.employee_data before and after every test."""
    Employee.employee_data.clear()
    yield
    Employee.employee_data.clear()


@pytest.fixture
def reset_logging():
    """Reset logging handlers after each test."""
    yield
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        handler.close()


# create_employee_from_string() Tests


@pytest.mark.parametrize(
    "input_string, expected_class, expected_id, expected_name, expected_position, expected_salary",
    [
        ("1,Alice,manager,80000", Manager, 1, "Alice", "Manager", 80000),
        ("2,Bob,developer,60000", Developer, 2, "Bob", "Developer", 60000),
        ("3,Charlie,intern,30000", Intern, 3, "Charlie", "Intern", 30000),
        ("4,Alice,MANAGER,80000", Manager, 4, "Alice", "Manager", 80000),
        ("5,Bob,Developer,60000", Developer, 5, "Bob", "Developer", 60000),
        ("6,Charlie,InTeRn,30000", Intern, 6, "Charlie", "Intern", 30000),
        ("7,Alice Smith,manager,80000", Manager, 7, "Alice Smith", "Manager", 80000),
        ("8,Alice,manager,80000.50", Manager, 8, "Alice", "Manager", 80000.50),
        ("9,Alice,manager,80000,extra,fields", Manager, 9, "Alice", "Manager", 80000),
    ],
)
def test__create_employee_from_string__valid_input__returns_employee_instance(
    input_string,
    expected_class,
    expected_id,
    expected_name,
    expected_position,
    expected_salary,
):
    result = create_employee_from_string(input_string)

    assert isinstance(result, expected_class)
    assert result.employee_id == expected_id
    assert result.name == expected_name
    assert result.position == expected_position
    assert result.salary == expected_salary


@pytest.mark.parametrize(
    "input_string, expected_exception, expected_message",
    [
        ("1,Alice,manager", IndexError, constants.INVALID_STRING_FORMAT),
        ("", ValueError, None),
        ("abc,Alice,manager,80000", ValueError, None),
        ("1,Alice,manager,abc", ValueError, None),
        ("1,Alice,manager,-1000", ValueError, None),
        # ("-1,Alice,manager,1000", ValueError, None),
    ],
)
def test__create_employee_from_string__invalid_input__throw_exception(
    input_string,
    expected_exception,
    expected_message,
):
    if expected_message:
        with pytest.raises(expected_exception, match=expected_message):
            create_employee_from_string(input_string)
    else:
        with pytest.raises(expected_exception):
            create_employee_from_string(input_string)


# add_employee() Tests


@pytest.mark.parametrize(
    "inputs, expected_id, expected_class",
    [
        (["1", "Alice", "developer", "50000"], 1, Developer),
        (["2", "Bob", "manager", "80000"], 2, Manager),
        (["3", "Charlie", "intern", "30000"], 3, Intern),
        (["4", "Alice", "DEVELOPER", "50000"], 4, Developer),
    ],
)
def test__add_employee__valid_input__add_to_register(inputs, expected_id, expected_class):
    with patch("builtins.input", side_effect=inputs):
        add_employee()

    assert Employee.number_of_employees() == 1
    assert expected_id in Employee.employee_data
    assert isinstance(Employee.employee_data[expected_id], expected_class)


@pytest.mark.parametrize(
    "inputs, expected_log",
    [
        (["0", "Alice", "developer", "50000"], constants.ID_SHOULD_BE_POSITIVE),
        (["-1", "Alice", "developer", "50000"], constants.ID_SHOULD_BE_POSITIVE),
        (["1", "", "developer", "50000"], constants.EMPLOYEE_NAME_EMPTY),
        (["1", "   ", "developer", "50000"], constants.EMPLOYEE_NAME_EMPTY),
        (["1", "Alice", "", "50000"], constants.EMPLOYEE_POSITION_EMPTY),
        (["1", "Alice", "ceo", "50000"], constants.INVALID_EMPLOYEE_POSITION_INPUT),
    ],
)
def test__add_employee__validation_errors__error_logged(inputs, expected_log, caplog):
    with patch("builtins.input", side_effect=inputs):
        with caplog.at_level(logging.WARNING):
            add_employee()

    assert expected_log in caplog.text
    assert Employee.number_of_employees() == 0


@pytest.mark.parametrize(
    "inputs",
    [
        ["abc", "Alice", "developer", "50000"],  # invalid ID
        ["1", "Alice", "developer", "abc"],  # invalid salary
    ],
)
def test__add_employee_invalid__invalid_input__error_logged(inputs, caplog):
    with patch("builtins.input", side_effect=inputs):
        with caplog.at_level(logging.ERROR):
            add_employee()

    assert "Invalid input" in caplog.text
    assert Employee.number_of_employees() == 0


def test__add_employee__duplicate_id__error_logged(caplog):
    # Arrange: pre-existing employee
    Manager(1, "Bob", 80000)

    logger_name = "src.assignment_7.employee_management"
    logger = logging.getLogger(logger_name)

    logger.propagate = True

    with patch("builtins.input", side_effect=["1", "Alice", "developer", "50000"]):
        with caplog.at_level(logging.WARNING):
            add_employee()

    assert constants.EMPLOYEE_ALREADY_EXISTS in caplog.text
    assert Employee.number_of_employees() == 1
    assert Employee.employee_data[1].name == "Bob"


# menu() Tests


def test__menu__called__displays_menu_correctly(capsys):

    menu()
    captured = capsys.readouterr()

    assert constants.MAIN_MENU in captured.out


# display_menu() Tests


def test__display_menu__called__shows_display_options(capsys):

    display_menu()
    captured = capsys.readouterr()

    assert constants.DISPLAY_MENU in captured.out


# add_employee_from_csv_string() Tests


@pytest.mark.parametrize(
    "input_string, expected_class",
    [
        ("1,Alice,developer,50000", Developer),
        ("  1,Alice,developer,50000  ", Developer),
        ("1,Alice,manager,80000", Manager),
        ("1,Alice,intern,30000", Intern),
    ],
)
def test__add_employee_from_csv_string__valid_input__returns_employee_instance(
    input_string, expected_class, caplog
):
    with patch("builtins.input", return_value=input_string):
        with caplog.at_level(logging.INFO):
            add_employee_from_csv_string()

    assert Employee.number_of_employees() == 1
    assert isinstance(Employee.employee_data[1], expected_class)
    assert constants.EMPLOYEE_CREATED in caplog.text


@pytest.mark.parametrize(
    "input_string, expected_exception",
    [
        ("1,Alice,ceo,50000", ValueError),  # invalid position
        ("1,Alice,developer", IndexError),  # missing salary
        ("abc,Alice,developer,50000", ValueError),  # invalid ID
        ("", ValueError),  # empty input → int("")
    ],
)
def test__add_employee_from_csv_string__invalid_input__throw_exception(
    input_string, expected_exception
):
    with patch("builtins.input", return_value=input_string):
        with pytest.raises(expected_exception):
            add_employee_from_csv_string()

    assert Employee.number_of_employees() == 0


# update_employee_salary() Tests


@pytest.mark.parametrize(
    "inputs, expected_salary",
    [
        (["1", "60000"], 60000),
        (["1", "55000.50"], 55000.50),
    ],
)
def test__update_employee_salary__valid_input__update_successful(inputs, expected_salary, caplog):
    Employee(1, "Alice", "Developer", 50000)

    with patch("builtins.input", side_effect=inputs):
        with caplog.at_level(logging.INFO):
            update_employee_salary()

    assert Employee.employee_data[1].salary == expected_salary
    assert constants.SALARY_UPDATED_SUCCESS in caplog.text


@pytest.mark.parametrize(
    "inputs, expected_log",
    [
        (["0", "60000"], constants.NEGATIVE_ID_ERROR),
        (["-1", "60000"], constants.NEGATIVE_ID_ERROR),
        (["1", "0"], constants.INVALID_ID_SALARY),
        (["1", "-1000"], constants.INVALID_ID_SALARY),
    ],
)
def test__update_employee_salary__validation_errors__error_logged(inputs, expected_log, caplog):
    Employee(1, "Alice", "Developer", 50000)

    with patch("builtins.input", side_effect=inputs):
        with caplog.at_level(logging.WARNING):
            update_employee_salary()

    assert expected_log in caplog.text


@pytest.mark.parametrize(
    "inputs",
    [
        ["999", "60000"],
        ["42", "50000"],
    ],
)
def test__update_employee_salary__nonexistent_id__not_found_logged(inputs, caplog):
    with patch("builtins.input", side_effect=inputs):
        with caplog.at_level(logging.WARNING):
            update_employee_salary()

    assert constants.EMPLOYEE_ID_NOT_FOUND in caplog.text


@pytest.mark.parametrize(
    "inputs",
    [
        ["abc", "60000"],
        ["1", "abc"],
    ],
)
def test__update_employee_salary__invalid_input__throw_exception(inputs):
    with patch("builtins.input", side_effect=inputs):
        with pytest.raises(ValueError, match=constants.INVALID_ID_SALARY):
            update_employee_salary()


# display_all_employee() Tests


@pytest.mark.parametrize(
    "choice, setup_fn, expected_names",
    [
        (
            "1",
            lambda: (Manager(1, "Alice", 80000), Developer(2, "Bob", 60000)),
            ["Alice", "Bob"],
        ),
        (
            "2",
            lambda: (
                Manager(1, "Alice", 80000),
                Developer(2, "Bob", 60000),
                Developer(3, "Charlie", 65000),
            ),
            ["Bob", "Charlie"],
        ),
        (
            "3",
            lambda: (
                Manager(1, "Alice", 80000),
                Intern(2, "Bob", 30000),
                Intern(3, "Charlie", 32000),
            ),
            ["Bob", "Charlie"],
        ),
    ],
)
def test__display_all_employee__valid_choices__all_employees_displayed(
    choice,
    setup_fn,
    expected_names,
    capsys,
):
    setup_fn()

    with patch("builtins.input", return_value=choice):
        display_all_employee()

    captured = capsys.readouterr().out
    for name in expected_names:
        assert name in captured


@pytest.mark.parametrize(
    "choice",
    ["0", "4", "abc"],
)
def test__display_all_employee__invalid_choice__throw_error(choice):
    with patch("builtins.input", return_value=choice):
        with pytest.raises(ValueError, match=constants.INVALID_DISPLAY_CHOICE):
            display_all_employee()


@pytest.mark.parametrize(
    "choice, setup_fn, expected_phrase",
    [
        (
            "2",
            lambda: (Manager(1, "Alice", 80000), Intern(2, "Bob", 30000)),
            "no developers",
        ),
        (
            "3",
            lambda: (Manager(1, "Alice", 80000), Developer(2, "Bob", 60000)),
            "no interns",
        ),
    ],
)
def test__display_all_employee__empty_groups__no_group(
    choice,
    setup_fn,
    expected_phrase,
    capsys,
):
    setup_fn()

    with patch("builtins.input", return_value=choice):
        display_all_employee()

    captured = capsys.readouterr().out.lower()
    assert expected_phrase in captured


# get_weekday() Tests


@pytest.mark.parametrize(
    "input_date, expected_result",
    [
        ("2025-12-29", True),  # weekday
        ("2025-12-27", False),  # weekend
        ("  2025-12-29  ", True),  # whitespace
    ],
)
def test__get_weekday__valid_dates__display_weekday_or_weekend(input_date, expected_result, capsys):
    with patch("builtins.input", return_value=input_date):
        get_weekday()

    expected_message = constants.DATE_WORKDAY_RESULT.format(
        input_date.strip(),
        expected_result,
    )
    captured = capsys.readouterr().out
    assert expected_message in captured


@pytest.mark.parametrize(
    "input_date",
    [
        "2025/12/29",
        "not-a-date",
        "",
    ],
)
def test__get_weekday__invalid_dates__thro_exception(input_date):
    with patch("builtins.input", return_value=input_date):
        with pytest.raises(ValueError, match="Invalid date string"):
            get_weekday()


# assign_mentor() Tests


@patch("builtins.input", side_effect=["1", "2"])
def test__assign_mentor__valid_input__assign_successful(mock_input, caplog):
    intern = Intern(1, "Alice", 30000)
    developer = Developer(2, "Bob", 60000)

    with caplog.at_level(logging.INFO):
        assign_mentor()

    assert intern.mentor_id == 2
    assert 1 in developer.mentees
    assert constants.MENTOR_ASSIGNED.format("Alice", "Bob") in caplog.text


@pytest.mark.parametrize(
    "inputs, setup_fn",
    [
        (["1", "2"], lambda: Developer(2, "Bob", 60000)),  # intern missing
        (["2", "1"], lambda: (Manager(1, "Alice", 80000), Manager(2, "Bob", 85000))),
    ],
)
def test__assign_mentor__invalid_intern__log_invalid_intern(inputs, setup_fn, caplog):
    setup_fn()

    with patch("builtins.input", side_effect=inputs):
        with caplog.at_level(logging.ERROR):
            assign_mentor()

    assert constants.INVALID_INTERN_ID in caplog.text


@pytest.mark.parametrize(
    "inputs, setup_fn",
    [
        (["1", "999"], lambda: Intern(1, "Alice", 30000)),  # missing developer
        (["1", "2"], lambda: (Intern(1, "Alice", 30000), Manager(2, "Bob", 80000))),
    ],
)
def test__assign_mentor__invalid_developer__log_invalid_developer(inputs, setup_fn, caplog):
    setup_fn()

    with patch("builtins.input", side_effect=inputs):
        with caplog.at_level(logging.ERROR):
            assign_mentor()

    assert "Invalid developer id" in caplog.text


@patch("builtins.input", side_effect=["1", "2"])
def test__assign_mentor__intern_already_has_mentor__log_already_assigned(mock_input, caplog):
    intern = Intern(1, "Alice", 30000)
    Developer(2, "Bob", 60000)
    Developer(3, "Charlie", 65000)

    intern.assign_mentor(2)  # Assign first mentor

    with caplog.at_level(logging.ERROR):
        assign_mentor()  # Try to assign second mentor

    assert "Intern already has a mentor" in caplog.text


# show_intern_mentor() Tests


@pytest.mark.parametrize(
    "setup_fn, expected_log",
    [
        (
            lambda: (
                Intern(1, "Alice", 30000),
                Developer(2, "Bob", 60000),
                Employee.employee_data[1].assign_mentor(2),  # type: ignore
            ),
            constants.INTERN_MENTOR_INFO.format("Alice", "Bob"),
        ),
        (
            lambda: Intern(1, "Alice", 30000),
            constants.INTERN_NO_MENTOR.format("Alice"),
        ),
    ],
)
def test__show_intern_mentor__valid_input__display_mentor_name(setup_fn, expected_log, capsys):
    setup_fn()

    with patch("builtins.input", return_value="1"):
        show_intern_mentor()

    captured = capsys.readouterr().out

    assert expected_log in captured


@pytest.mark.parametrize(
    "input_value, setup_fn, expected_log",
    [
        ("999", lambda: None, constants.INVALID_INTERN_ID),
        ("1", lambda: Developer(1, "Alice", 60000), constants.INVALID_INTERN_ID),
        ("abc", lambda: None, constants.INVALID_GENERIC_INPUT),
    ],
)
def test__show_intern_mentor__invalid_input__logs_error(
    input_value,
    setup_fn,
    expected_log,
    caplog,
):
    setup_fn()

    with patch("builtins.input", return_value=input_value):
        with caplog.at_level(logging.ERROR):
            show_intern_mentor()

    assert expected_log in caplog.text


# show_developer_mentees() Tests


@pytest.mark.parametrize(
    "setup_fn, expected_out",
    [
        (
            # Multiple mentees
            lambda: (
                Intern(1, "Alice", 30000),
                Intern(3, "Charlie", 32000),
                Developer(2, "Bob", 60000),
                Employee.employee_data[1].assign_mentor(2),  # type: ignore
                Employee.employee_data[3].assign_mentor(2),  # type: ignore
            ),
            [
                constants.DEVELOPER_MENTEES_HEADER.format("Bob"),
                "Alice",
                "Charlie",
            ],
        ),
        (
            # Single mentee
            lambda: (
                Intern(1, "Alice", 30000),
                Developer(2, "Bob", 60000),
                Employee.employee_data[1].assign_mentor(2),  # type: ignore
            ),
            [
                constants.DEVELOPER_MENTEES_HEADER.format("Bob"),
                "Alice",
            ],
        ),
        (
            # No mentees
            lambda: Developer(2, "Bob", 60000),
            [
                constants.DEVELOPER_NO_MENTEES.format("Bob"),
            ],
        ),
    ],
)
def test__show_developer_mentees__valid_cases__displays_mentees_list(
    setup_fn, expected_out, capsys
):
    setup_fn()

    with patch("builtins.input", return_value="2"):
        show_developer_mentees()

    captured = capsys.readouterr().out

    for log in expected_out:
        assert log in captured


@pytest.mark.parametrize(
    "input_value, setup_fn, expected_log",
    [
        ("999", lambda: None, constants.INVALID_DEVELOPER_ID),
        ("1", lambda: Manager(1, "Alice", 80000), constants.INVALID_DEVELOPER_ID),
        ("abc", lambda: None, constants.INVALID_GENERIC_INPUT),
    ],
)
def test__show_developer_mentees__invalid_cases__logs_invalid_message(
    input_value,
    setup_fn,
    expected_log,
    caplog,
):
    setup_fn()

    with patch("builtins.input", return_value=input_value):
        with caplog.at_level(logging.ERROR):
            show_developer_mentees()

    assert expected_log in caplog.text


# initialise_logger() Tests


def test__initialise_logger__sets_root_level(reset_logging, tmp_path):
    log_file = tmp_path / "test_log.txt"

    initialise_logger(log_file)

    root_logger = logging.getLogger()
    assert root_logger.level == logging.DEBUG


def test__initialise_logger__is_idempotent(reset_logging, tmp_path):
    log_file = tmp_path / "test_log.txt"

    root_logger = logging.getLogger()
    initial_handler_count = len(root_logger.handlers)

    initialise_logger(log_file)
    initialise_logger(log_file)

    assert len(root_logger.handlers) == initial_handler_count


def test__initialise_logger__adds_file_handler_when_no_handlers(tmp_path):
    log_file = tmp_path / "test_log.txt"

    root_logger = logging.getLogger()

    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    initialise_logger(log_file)

    file_handlers = [h for h in root_logger.handlers if isinstance(h, logging.FileHandler)]

    assert len(file_handlers) == 1
    assert log_file.exists()
