import json
from pathlib import Path
from typing import Any, Dict


def  json_analyzer(json_path : str) -> Any:
    try:
        path = Path(json_path)
        with open (path, 'r') as file:
            data = json.load(file)
        val = json.dumps(data, indent=4)
        return val
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {json_path} was not found.")
    except json.JSONDecodeError:
        raise ValueError(f"The file at {json_path} is not a valid JSON file.")

if __name__ == "__main__":
    path = input("Enter the JSON file path: ")
    json_data = json_analyzer(path)
    print("JSON Data:", json_data)