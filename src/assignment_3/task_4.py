"""Module extracting and flattening JSON files."""

import json
from pathlib import Path
from typing import Any, Dict


def flatten_nested_json_analyzer(data: Dict[str, Any], parent_key: str = "") -> Dict[str, Any]:
    """Flattens the nested JSON structure into a single-level dictionary.

    Args:
        data : The nested JSON data.
        parent_key : Parent key. default is "".

    Returns:
        Dict: Flatten JSON structure.
    """
    flatten_json: Dict[str, Any] = {}
    for key, value in data.items():
        if isinstance(value, dict):
            flatten_json = flatten_json | flatten_nested_json_analyzer(
                value, parent_key + key + "_"
            )
        else:
            flatten_json[parent_key + key] = value
    return flatten_json


def json_analyzer(json_path: str) -> Dict[str, Any]:
    """JSON data extracted from the file.

    Args:
        json_path : JSON file path.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file contains invalid JSON.

    Returns:
        Dict: Extracted JSON data.
    """
    path = Path(json_path)

    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in file {path}: {exc}") from exc

    return data


if __name__ == "__main__":
    path = input("Enter the JSON file path: ")
    try:
        json_data = json_analyzer(path)
    except Exception as exc:
        print("Error:", exc)
    else:
        for key, value in flatten_nested_json_analyzer(json_data).items():
            print(f"{key}: {value}")
