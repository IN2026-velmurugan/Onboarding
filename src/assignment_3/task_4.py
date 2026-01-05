"""Functions for extracting and flattening JSON files."""

import json
from pathlib import Path
from typing import Any

# Constants
DATA_ERROR_PREFIX = "Data error:"
FILE_ENCODING = "utf-8"
FILE_ERROR_PREFIX = "File error:"
FILE_OPEN_MODE = "r"
INPUT_JSON_PATH_PROMPT = "Enter the JSON file path: "
INTERRUPT_MESSAGE = "Operation cancelled by user"
INVALID_JSON_ERROR = "Invalid JSON in file {}: {}"
JSON_FILE_NOT_FOUND = "JSON file not found: {}"
JSON_ROOT_NOT_LIST = "JSON root must be a list of objects"
KEY_SEPARATOR = "_"


def flatten_nested_json_analyzer(data: dict[str, Any], parent_key: str = "") -> dict[str, Any]:
    """Flatten the nested JSON structure into a single-level dictionary.

    Args:
        data : The JSON structure that may contain nested structure.
        parent_key : The base key used for building hierarchical keys during flattening.
                    Default is "".

    Returns:
        Flatten JSON structure.
    """
    flatten_json: dict[str, Any] = {}

    for key, value in data.items():
        if isinstance(value, dict):
            flatten_json.update(
                flatten_nested_json_analyzer(
                    value,
                    parent_key + key + KEY_SEPARATOR,
                )
            )
        else:
            flatten_json[parent_key + key] = value

    return flatten_json


def json_analyzer(json_path: str) -> list[dict[str, Any]]:
    """JSON data extracted from the file.

    Args:
        json_path : JSON file path.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file contains invalid JSON.

    Returns:
        JSON data from the file.
    """
    path = Path(json_path)

    if not path.exists():
        raise FileNotFoundError(JSON_FILE_NOT_FOUND.format(path))

    try:
        with path.open(FILE_OPEN_MODE, encoding=FILE_ENCODING) as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError(JSON_ROOT_NOT_LIST)

    except json.JSONDecodeError as e:
        raise ValueError(INVALID_JSON_ERROR.format(path, e)) from e

    return data


if __name__ == "__main__":
    path = input(INPUT_JSON_PATH_PROMPT)

    try:
        json_data = json_analyzer(path)

    except FileNotFoundError as e:
        print(FILE_ERROR_PREFIX, e)

    except ValueError as e:
        print(DATA_ERROR_PREFIX, e)

    except KeyboardInterrupt:
        print(INTERRUPT_MESSAGE)

    else:
        for dictionary in json_data:
            for key, value in flatten_nested_json_analyzer(dictionary).items():
                print(f"{key}: {value}")
