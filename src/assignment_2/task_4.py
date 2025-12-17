"""This module demonstrates immutability of strings and integers in Python."""

string_1 = "Hello, this is a test string for checking immutability."

try:
    string_1[0] = "h"  # type: ignore
except Exception as e:
    print("causes Error because string is immutable:", e)

integer_1 = 1000
try:
    integer_1[0] = 1  # type: ignore
except Exception as e:
    print("causes Error because integer is immutable:", e)
