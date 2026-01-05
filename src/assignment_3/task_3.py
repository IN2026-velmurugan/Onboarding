"""Navigate through the directory and count the number of files."""

import os
from pathlib import Path

# Constants
ERROR_PATH_NOT_DIRECTORY = "Path is not a directory"
ERROR_PATH_NOT_EXIST = "Path does not exist"
FILESYSTEM_ERROR_PREFIX = "Filesystem error: {}"
INPUT_ERROR_PREFIX = "Input error: {}"
INPUT_PATH_PROMPT = "Enter the path: "
INTERRUPT_MESSAGE = "Program was interrupted."
PRINT_OS_COUNT = "Total number of files using os: {}"
PRINT_PATHLIB_COUNT = "Total number of files using pathlib: {}"


def navigate_system_using_os(path: Path) -> int:
    """Navigate through the directory recursively and count files using os library.

    Args:
        path : Parent file directory path.

    Returns:
        Count of files inside the file directory provided..
    """
    result = 0
    for root, dirs, files in os.walk(path):
        result += len(files)

    return result


def navigate_system_using_pathlib(path: Path) -> int:
    """Navigate through the directory recursively and count files using pathlib library.

    Args:
        path : Parent file directory path.

    Returns:
        Count of files inside the file directory provided.
    """
    result = 0
    for item in path.iterdir():
        if item.is_dir():
            result += navigate_system_using_pathlib(item)
        else:
            result += 1

    return result


if __name__ == "__main__":
    try:
        path = Path(input(INPUT_PATH_PROMPT).replace("\\", "/"))

        if not path.exists():
            raise ValueError(ERROR_PATH_NOT_EXIST)

        if not path.is_dir():
            raise ValueError(ERROR_PATH_NOT_DIRECTORY)

        path_count = navigate_system_using_pathlib(path)
        os_count = navigate_system_using_os(path)

        print(PRINT_OS_COUNT.format(os_count))
        print(PRINT_PATHLIB_COUNT.format(path_count))

    except KeyboardInterrupt:
        print(INTERRUPT_MESSAGE)

    except ValueError as e:
        print(INPUT_ERROR_PREFIX.format(e))

    except (PermissionError, OSError) as e:
        print(FILESYSTEM_ERROR_PREFIX.format(e))
