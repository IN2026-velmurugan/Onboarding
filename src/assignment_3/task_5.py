"""Mock database operation performed on a text file."""

import json
from datetime import datetime
from typing import Any, Optional

DATABASE_ERROR_PREFIX = "Database error:"
DB_FILE = "database.json"

ERROR_CREATE_DATA_MISSING = "Data must be provided for CREATE operation."
ERROR_DB_FILE_NOT_FOUND = "Database file not found."
ERROR_DELETE_CONDITION_MISSING = "Condition must be provided for DELETE operation."
ERROR_DELETE_FAILED = "An error occurred while deleting from the database."
ERROR_INVALID_JSON_INPUT = "Invalid JSON input."
ERROR_UPDATE_DATA_MISSING = "Data and condition must be provided for UPDATE operation."
ERROR_UPDATE_FAILED = "An error occurred while updating the database."

EXAMPLE_JSON_FULL = """Example: {"id":2,"name":"res","dict":{"nested":"value","list":[1,2,3]}}"""
EXAMPLE_JSON_ID = """Example: {"id": 1}"""
EXAMPLE_JSON_UPDATE = """Example: {"name": "Jane"}"""

EXIT_MESSAGE = "\nOperation cancelled by user."

INPUT_ERROR_PREFIX = "Input error:"

MENU = """
1 - To Create JSON line.
2 - To Read JSON line.
3 - To Update JSON line.
4 - To Delete JSON line.
0 - To Exit.
"""

MSG_INVALID_CHOICE = "Invalid choice. Try again."
RECORD_CREATED = "Record created successfully."
RECORDS_DELETED = "{} record(s) deleted successfully."
RECORDS_UPDATED = "{} record(s) updated successfully."

OP_CREATE = "CREATE"
OP_DELETE = "DELETE"
OP_READ = "READ"
OP_UPDATE = "UPDATE"

PROMPT_CREATE_JSON = "Enter a JSON object:"
PROMPT_DELETE_CONDITION = "\nEnter DELETE condition."
PROMPT_JSON_INPUT = "JSON > "
PROMPT_MENU_CHOICE = "Enter your choice (0-4):"
PROMPT_UPDATE_CONDITION = "\nEnter UPDATE condition."
PROMPT_UPDATE_VALUES = "\nEnter new values."

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def time_stamp() -> str:
    """Get the current timestamp.

    Returns:
        Return the time stamp
    """
    return datetime.now().strftime(TIMESTAMP_FORMAT)


def create_record(data: Optional[dict[str, Any]] = None) -> None:
    """Add the JSON line to the file.

    Args:
        data : JSON data. Defaults to None.
    """
    if data is None:
        raise ValueError(ERROR_CREATE_DATA_MISSING)

    with open(DB_FILE, "a", encoding="utf-8") as db_file:
        db_file.write(json.dumps(data) + "\n")

    print(time_stamp(), RECORD_CREATED)


def display_record() -> None:
    """Display the contents of the file.

    Raises:
        FileNotFoundError : When the file is not found.
    """
    try:
        with open(DB_FILE, "r") as db_file:
            for line in db_file:
                if not line.strip():
                    continue
                print(json.loads(line.strip()))
    except FileNotFoundError as ex:
        raise FileNotFoundError(ERROR_DB_FILE_NOT_FOUND) from ex


def update_record(
    data: Optional[dict[str, Any]] = None, condition: Optional[dict[str, Any]] = None
) -> None:
    """Update the JSON line.

    Args:
        data : Data to be updated. Defaults to None.
        condition : The line to be updated. Defaults to None.

    Raises:
        ValueError: If data is not present
        FileNotFoundError: When the file is not found.
        Exception: Uncaught exception.
    """
    if data is None or condition is None:
        raise ValueError(ERROR_UPDATE_DATA_MISSING)

    try:
        lines_updated = 0
        with open(DB_FILE, "r") as db_file:
            lines = db_file.readlines()

        with open(DB_FILE, "w") as db_file:
            for line in lines:
                if not line.strip():
                    continue
                record = json.loads(line.strip())
                if all(record.get(k) == v for k, v in condition.items()):
                    record.update(data)
                    lines_updated += 1
                db_file.write(json.dumps(record) + "\n")

        print(time_stamp(), RECORDS_UPDATED.format(lines_updated))

    except FileNotFoundError as ex:
        raise FileNotFoundError(ERROR_DB_FILE_NOT_FOUND) from ex
    except Exception as exc:
        raise Exception(ERROR_UPDATE_FAILED) from exc


def delete_record(condition: Optional[dict[str, Any]] = None) -> None:
    """Delete a JSON line.

    Args:
        condition : The line to be deleted. Defaults to None.

    Raises:
        ValueError: If data is not provided.
        FileNotFoundError: When the file is not found.
        Exception: Uncaught exception.
    """
    if condition is None:
        raise ValueError(ERROR_DELETE_CONDITION_MISSING)

    try:
        lines_deleted = 0
        with open(DB_FILE, "r") as db_file:
            lines = db_file.readlines()

        with open(DB_FILE, "w") as db_file:
            for line in lines:
                if not line.strip():
                    continue
                record = json.loads(line.strip())
                if all(record.get(k) == v for k, v in condition.items()):
                    lines_deleted += 1
                else:
                    db_file.write(json.dumps(record) + "\n")

        print(time_stamp(), RECORDS_DELETED.format(lines_deleted))

    except FileNotFoundError as ex:
        raise FileNotFoundError(ERROR_DB_FILE_NOT_FOUND) from ex
    except Exception as exc:
        raise Exception(ERROR_DELETE_FAILED) from exc


def manage_database(
    args: str,
    data: Optional[dict[str, Any]] = None,
    condition: Optional[dict[str, Any]] = None,
):
    """Manage the database operation.

    Args:
        args : Database argument.
        data : Data to be updated. Defaults to None.
        condition : The line to be updated. Defaults to None.
    """
    if args == OP_CREATE:
        create_record(data)
    elif args == OP_READ:
        display_record()
    elif args == OP_UPDATE:
        update_record(data, condition)
    elif args == OP_DELETE:
        delete_record(condition)


def get_json_string() -> dict[str, Any]:
    """Get the valid JSON string from the user.

    Raises:
        ValueError: If the JSON input is not valid.

    Returns:
        JSON string as Dictionary.
    """
    raw_input_str = input(PROMPT_JSON_INPUT)

    try:
        return json.loads(raw_input_str)
    except json.JSONDecodeError as exc:
        raise ValueError(ERROR_INVALID_JSON_INPUT) from exc


def run_create_command() -> None:
    """Create a line in database."""
    print(PROMPT_CREATE_JSON)
    print(EXAMPLE_JSON_FULL)
    json_line = get_json_string()
    manage_database(OP_CREATE, json_line)


def run_update_command() -> None:
    """Update a line in the database."""
    manage_database(OP_READ)

    print(PROMPT_UPDATE_CONDITION)
    print(EXAMPLE_JSON_ID)
    condition = get_json_string()

    print(PROMPT_UPDATE_VALUES)
    print(EXAMPLE_JSON_UPDATE)
    data = get_json_string()

    manage_database(OP_UPDATE, data, condition)


def run_delete_command() -> None:
    """Delete a line on database."""
    manage_database(OP_READ)

    print(PROMPT_DELETE_CONDITION)
    print(EXAMPLE_JSON_ID)
    condition = get_json_string()

    manage_database(OP_DELETE, condition=condition)


if __name__ == "__main__":
    choice = -1
    while choice != 0:
        try:
            print(MENU)
            choice = int(input(PROMPT_MENU_CHOICE))

            if choice == 0:
                break
            elif choice == 1:
                run_create_command()
            elif choice == 2:
                manage_database(OP_READ)
            elif choice == 3:
                run_update_command()
            elif choice == 4:
                run_delete_command()
            else:
                print(MSG_INVALID_CHOICE)

        except ValueError as exc:
            print(INPUT_ERROR_PREFIX, exc)
        except FileNotFoundError as exc:
            print(DATABASE_ERROR_PREFIX, exc)
        except KeyboardInterrupt:
            print(EXIT_MESSAGE)
