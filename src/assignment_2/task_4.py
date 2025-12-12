string_1 = "Hello, this is a test string for checking immutability."  # noqa: D100 - Missing docstring in public module (auto-generated noqa)

try:
    string_1[0] = "h"
except Exception as e:
    print("causes Error because string is immutable:", e)

integer_1 = 1000
try:
    integer_1[0] = 1
except Exception as e:
    print("causes Error because integer is immutable:", e)
