"""Interactive console application to demonstrate the TechFellowTools package."""

from pathlib import Path

from src.assignment_6.TechFellowTools import mean
from src.assignment_6.TechFellowTools.data_tools import read_csv
from src.assignment_6.TechFellowTools.math_tools import matrix_operations as mo
from src.assignment_6.TechFellowTools.string_tools.string_transformations import compress_string

ERROR_ATTEMPT_EXCEEDED = "Attempt exceeded. Please try again."
ERROR_FILE_OPERATION = "File error : {}"
ERROR_INVALID_OPERATION = "Invalid operation : {}"

HEADER_CSV = "\n--- CSV Data Tools Demo ---"
HEADER_MATH = "\n--- Math Utilities Demo ---"
HEADER_MATRIX = "\n--- Matrix Operations Demo ---"
HEADER_STRING = "\n--- String Utilities Demo ---"

KEYBOARD_INTERRUPT = "Exiting the program !!!"

LABEL_COMPRESSED = "Compressed String:"
LABEL_CSV_CONTENT = "CSV Content:"
LABEL_MATRIX_ADD = "Matrix Addition:"
LABEL_MATRIX_MUL = "Matrix Multiplication:"
LABEL_MEAN = "Mean:"

MENU_TEXT = """
=== TechFellowTools Demo Console ===
1. Math Utilities (Mean)
2. Matrix Operations
3. String Utilities
4. CSV Data Tools
0. Exit
"""

MSG_EXIT = "Exiting TechFellowTools Demo. Goodbye!"
MSG_INVALID_CHOICE = "Invalid choice. Please select 1–5."

PROMPT_CSV_PATH = "Enter CSV file path: "
PROMPT_MATRIX_A_INFO = "Enter values for 2x2 Matrix A (row-wise):"
PROMPT_MATRIX_A_VALUES = "A (4 values): "
PROMPT_MATRIX_B_INFO = "Enter values for 2x2 Matrix B (row-wise):"
PROMPT_MATRIX_B_VALUES = "B (4 values): "
PROMPT_MENU_CHOICE = "Enter your choice: "
PROMPT_NUMBERS = "Enter numbers separated by space: "
PROMPT_STRING = "Enter a string to compress: "

UNKNOWN_ERROR = "Unknown error occurred in the application shutting down. {}"


def demo_math() -> None:
    """Demonstrate use of mean from math_tools."""
    print(HEADER_MATH)
    values = input(PROMPT_NUMBERS).split()
    numbers = [float(v) for v in values]
    print(LABEL_MEAN, mean(numbers))


def demo_matrix() -> None:
    """Demonstrate the matrix operation using the math_tools."""
    print(HEADER_MATRIX)

    print(PROMPT_MATRIX_A_INFO)
    a = list(map(float, input(PROMPT_MATRIX_A_VALUES).split()))
    matrix_a = [[a[0], a[1]], [a[2], a[3]]]

    print(PROMPT_MATRIX_B_INFO)
    b = list(map(float, input(PROMPT_MATRIX_B_VALUES).split()))
    matrix_b = [[b[0], b[1]], [b[2], b[3]]]

    print(LABEL_MATRIX_ADD, mo.add_matrices(matrix_a, matrix_b))
    print(LABEL_MATRIX_MUL, mo.mul_matrices(matrix_a, matrix_b))


def demo_string() -> None:
    """Demonstrate the use of string_tool module."""
    print(HEADER_STRING)
    text = input(PROMPT_STRING)
    print(LABEL_COMPRESSED, compress_string(text))


def demo_csv() -> None:
    """Demonstrate the use of data_tool module."""
    print(HEADER_CSV)
    path = Path(input(PROMPT_CSV_PATH))
    print(LABEL_CSV_CONTENT)
    print(read_csv(path))


menu_action = {
    1: demo_math,
    2: demo_matrix,
    3: demo_string,
    4: demo_csv,
}


def run_tool() -> None:
    """Main menu operation to demonstrate the the `TechFellowTools` package."""
    choice = -1
    count = 0
    try:
        while choice != 0 and count < 5:
            print(MENU_TEXT)
            try:
                choice = int(input(PROMPT_MENU_CHOICE))
            except ValueError as e:
                count += 1
                print(ERROR_INVALID_OPERATION.format(e))
                continue

            if choice == 0:
                print(MSG_EXIT)
                break

            action = menu_action.get(choice)
            if not action:
                count += 1
                print(MSG_INVALID_CHOICE)
                continue

            try:
                action()
            except ValueError as e:
                print(ERROR_INVALID_OPERATION.format(e))
            except FileExistsError as e:
                print(ERROR_FILE_OPERATION.format(e))
        else:
            if count == 5:
                raise ValueError(ERROR_ATTEMPT_EXCEEDED)
    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print(KEYBOARD_INTERRUPT)
    except Exception as e:
        print(UNKNOWN_ERROR.format(e))


if __name__ == "__main__":
    run_tool()
