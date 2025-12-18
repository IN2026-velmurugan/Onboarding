"""Module contains mock database operation performed on a text file."""

import json
from datetime import datetime
from typing import Any, Dict, Optional

DB_FILE = "database.txt"


def time_stamp() -> str:
    """Gets the current timestamp.

    Returns:
        Return the time stamp
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_line(data: Optional[Dict[str, Any]] = None):
    """Adds the JSON line to the file.

    Args:
        data : JSON data. Defaults to None.

    Raises:
        ValueError : If data is not provided.
        FileNotFoundError : When the file is not found.
        Exception : Uncaught exception.
    """
    if data is None:
        raise ValueError("Data must be provided for CREATE operation.")
    try:
        with open(DB_FILE, "a") as db_file:
            db_file.write(json.dumps(data) + "\n")
    except FileNotFoundError as ex:
        raise FileNotFoundError("Database file not found.") from ex
    except Exception as exc:
        raise Exception(f"An error occurred while writing to the database.") from exc

    print(time_stamp() + " Record created successfully.")


def read_lines():
    """Reads and displays the contents of the file.

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
        raise FileNotFoundError("Database file not found.") from ex


def update_line(data: Optional[Dict[str, Any]] = None, condition: Optional[Dict[str, Any]] = None):
    """Updates the JSON line.

    Args:
        data : Data to be updated. Defaults to None.
        condition : The line to be updated. Defaults to None.

    Raises:
        ValueError: If data is not present
        FileNotFoundError: When the file is not found.
        Exception: Uncaught exception.
    """
    if data is None or condition is None:
        raise ValueError("Data and condition must be provided for UPDATE operation.")
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

        print(time_stamp() + f" {lines_updated} record(s) updated successfully.")
    except FileNotFoundError as ex:
        raise FileNotFoundError("Database file not found.") from ex
    except Exception as exc:
        raise Exception(f"An error occurred while updating the database.") from exc


def delete_line(condition: Optional[Dict[str, Any]] = None):
    """Deletes the JSON line.

    Args:
        condition : The line to be deleted. Defaults to None.

    Raises:
        ValueError: If data is not provided.
        FileNotFoundError: When the file is not found.
        Exception: Uncaught exception.
    """
    if condition is None:
        raise ValueError("Condition must be provided for DELETE operation.")
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

        print(time_stamp() + f" {lines_deleted} record(s) deleted successfully.")
    except FileNotFoundError as ex:
        raise FileNotFoundError("Database file not found.") from ex
    except Exception as exc:
        raise Exception(f"An error occurred while deleting from the database.") from exc


def database_manager(
    args: str,
    data: Optional[Dict[str, Any]] = None,
    condition: Optional[Dict[str, Any]] = None,
):
    """Manages the database operation.

    Args:
        args : Database argument.
        data : Data to be updated. Defaults to None.
        condition : The line to be updated. Defaults to None.
    """
    try:
        if args == "CREATE":
            create_line(data)
        elif args == "READ":
            read_lines()
        elif args == "UPDATE":
            update_line(data, condition)
        elif args == "DELETE":
            delete_line(condition)
    except Exception:
        raise


def get_json_string() -> Dict[str, Any]:
    """Gets the valid JSON string from the user.

    Raises:
        ValueError: if the JSON input is not valid.

    Returns:
        JSON string as Dictionary.
    """
    raw_input_str = input("JSON > ")

    try:
        data: Dict[str, Any] = json.loads(raw_input_str)
        return data
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON input") from exc


if __name__ == "__main__":
    try:
        while True:
            print("\n1 - To Create JSON line")
            print("2 - To Read JSON line")
            print("3 - To Update JSON line")
            print("4 - To Delete JSON line")
            print("0 - To Exit")

            choice = int(input("Enter your choice: "))

            if choice == 0:
                break

            elif choice == 1:
                print("Enter a JSON object:")
                print('Example: {"id":2,"name":"res","dict":{"nested":"value","list":[1,2,3]}}')
                json_line = get_json_string()
                database_manager("CREATE", json_line)

            elif choice == 2:
                database_manager("READ")

            elif choice == 3:
                database_manager("READ")

                print("\nEnter UPDATE condition")
                print('Example: {"id": 1}')
                condition = get_json_string()

                print("\nEnter new values")
                print('Example: {"name": "Jane"}')
                data = get_json_string()

                database_manager("UPDATE", data, condition)

            elif choice == 4:
                database_manager("READ")

                print("\nEnter DELETE condition")
                print('Example: {"id": 1}')
                condition = get_json_string()

                database_manager("DELETE", condition=condition)

            else:
                print("Invalid choice. Try again.")

    except Exception as exc:
        print(f"Error: {exc}")
