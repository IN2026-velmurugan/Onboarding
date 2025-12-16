"""Module to navigate through the directory and count files."""

import os
from pathlib import Path


def system_navigator_using_os(path: str) -> int:
    """Navigates through the directory recursively and count files using os library.

    Args:
        path : Parent file directory path.

    Returns:
        Count of files.
    """
    result = 0
    for item in os.listdir(path):
        abs_path = os.path.join(path, item)
        if os.path.isdir(abs_path):
            result += system_navigator_using_os(abs_path)
        else:
            result += 1

    return result


def system_navigator_using_pathlib(path: Path) -> int:
    """Navigates through the directory recursively and count files using pathlib library.

    Args:
        path : Parent file directory path.

    Returns:
        Count of files inside the file directory provided.
    """
    result = 0
    for item in list(path.iterdir()):
        if item.is_dir():
            result += system_navigator_using_pathlib(item)
        else:
            result += 1

    return result


if __name__ == "__main__":
    path = input("Enter the path: ")
    os_count = system_navigator_using_pathlib(Path(path.replace("\\", "/")))
    path_count = system_navigator_using_os(path.replace("\\", "/"))
    print(f"Total number of files using os: {os_count}")
    print(f"Total number of files using pathlib: {os_count}")
