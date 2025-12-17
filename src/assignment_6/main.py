"""Demonstration script for the TechFellowTools package."""

from tech_fellow_tools import mean  # type: ignore
from tech_fellow_tools.data_tools import read_csv  # type: ignore
from tech_fellow_tools.math_tools import matrix_operations as mo  # type: ignore
from tech_fellow_tools.string_tools import compress_string  # type: ignore

# from tech_fellow_tools.string_tools import *  # bad practice

# Math functions
print("Mean:", mean([10, 20, 30]))

matrix_a = [[1.0, 2.0], [3.0, 4.0]]
matrix_b = [[5.0, 6.0], [7.0, 8.0]]
print("Matrix Addition:", mo.matrix_addition(matrix_a, matrix_b))

# String functions
print("Uppercase:", compress_string("tech fellow tools"))  # type: ignore

# Data tools
print("CSV Data:", read_csv("data.csv"))
