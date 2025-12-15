"""Module to navigate through the directory and count files."""

import os


def system_navigator(path: str) -> int:
    """To navigate through the directory and count files.

    Args:
        path (str): Parent file directory path.

    Returns:
        int: Count of files.
    """
    result = 0
    for item in os.listdir(path):
        if os.path.isdir(path + "/" + item):
            result += system_navigator(path + "/" + item)
        else:
            result += 1

    return result


if __name__ == "__main__":
    path = input("Enter the path: ")
    count = system_navigator(path.replace("\\", "/"))
    print(f"Total number of files: {count}")
