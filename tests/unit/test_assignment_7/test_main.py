import builtins
import logging
from unittest.mock import MagicMock, patch

import pytest
import src.assignment_7.main as main_module
from src.assignment_7 import constants


@pytest.fixture(autouse=True)
def isolate_main(monkeypatch):
    """Prevent real logger initialization and filesystem access."""
    monkeypatch.setattr(main_module, "initialise_logger", MagicMock())
    main_module.LOGGER = logging.getLogger("test-main")
    yield


# Exit path
def test_main_exit_immediately(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "0")

    with patch.object(main_module.LOGGER, "info") as mock_info:
        main_module.main()  # type: ignore

    mock_info.assert_called_with(constants.EXIT_SUCCESS)


# Menu routing
@pytest.mark.parametrize(
    "choice, function_name",
    [
        ("1", "add_employee"),
        ("3", "update_employee_salary"),
        ("4", "display_all_employee"),
        ("5", "get_weekday"),
        ("6", "add_employee_from_csv_string"),
        ("7", "assign_mentor"),
        ("8", "show_intern_mentor"),
        ("9", "show_developer_mentees"),
    ],
)
def test_main_routes_menu_options(monkeypatch, choice, function_name):
    mock_func = MagicMock()
    monkeypatch.setattr(main_module, function_name, mock_func)

    inputs = iter([choice, "0"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    main_module.main()  # type: ignore

    mock_func.assert_called_once()


# Invalid input (non-numeric)
def test_main_invalid_choice_logs_error(monkeypatch):
    inputs = iter(["abc", "0"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    with patch.object(main_module.LOGGER, "error") as mock_error:
        main_module.main()  # type: ignore

    mock_error.assert_called_with(constants.INVALID_CHOICE_ERROR)


# Invalid input (out of range)


def test_main_out_of_range_choice(monkeypatch):
    inputs = iter(["99", "0"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    with patch.object(main_module.LOGGER, "error") as mock_error:
        main_module.main()  # type: ignore

    mock_error.assert_called_with(constants.INVALID_CHOICE_ERROR)


# KeyboardInterrupt handling


def test_main_keyboard_interrupt(monkeypatch):
    def raise_interrupt(_):
        raise KeyboardInterrupt

    monkeypatch.setattr(builtins, "input", raise_interrupt)

    with patch.object(main_module.LOGGER, "info") as mock_info:
        main_module.main()  # type: ignore

    mock_info.assert_called_with("Application interrupted by user.")
