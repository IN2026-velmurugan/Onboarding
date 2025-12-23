"""Interactive console application to demonstrate the TechFellowTools package."""

from pathlib import Path

from src.assignment_6.TechFellowTools import mean
from src.assignment_6.TechFellowTools.data_tools import read_csv
from src.assignment_6.TechFellowTools.math_tools import matrix_operations as mo
from src.assignment_6.TechFellowTools.string_tools.string_transformations import compress_string


def show_menu() -> None:
    """Display menu for the user for demo."""
    print("\n=== TechFellowTools Demo Console ===")
    print("1. Math Utilities (Mean)")
    print("2. Matrix Operations")
    print("3. String Utilities")
    print("4. CSV Data Tools")
    print("5. Exit")


def demo_math() -> None:
    """Demonstrate use of mean from math_tools."""
    print("\n--- Math Utilities Demo ---")
    values = input("Enter numbers separated by space: ").split()
    numbers = [float(v) for v in values]
    print("Mean:", mean(numbers))


def demo_matrix() -> None:
    """Demonstrates the matrix operation using the math_tools."""
    print("\n--- Matrix Operations Demo ---")
    print("Enter values for 2x2 Matrix A (row-wise):")
    a = list(map(float, input("A (4 values): ").split()))
    matrix_a = [[a[0], a[1]], [a[2], a[3]]]

    print("Enter values for 2x2 Matrix B (row-wise):")
    b = list(map(float, input("B (4 values): ").split()))
    matrix_b = [[b[0], b[1]], [b[2], b[3]]]

    print("Matrix Addition:", mo.matrix_addition(matrix_a, matrix_b))
    print("Matrix Multiplication:", mo.matrix_multiplication(matrix_a, matrix_b))


def demo_string() -> None:
    """Demonstrates the use of string_tool module."""
    print("\n--- String Utilities Demo ---")
    text = input("Enter a string to compress: ")
    print("Compressed String:", compress_string(text))


def demo_csv() -> None:
    """Demonstrates the use of data_tool module."""
    print("\n--- CSV Data Tools Demo ---")
    path = Path(input("Enter CSV file path: "))
    print("CSV Content:")
    print(read_csv(path))


def main() -> None:
    """Main menu operation based on the user choice."""
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            demo_math()
        elif choice == "2":
            demo_matrix()
        elif choice == "3":
            demo_string()
        elif choice == "4":
            demo_csv()
        elif choice == "5":
            print("Exiting TechFellowTools Demo. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1–5.")


if __name__ == "__main__":
    main()
