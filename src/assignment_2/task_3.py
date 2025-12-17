"""The module evaluates multiple expressions to demonstrate the operator precedence."""

result_1 = 10**2 / 5 + 2 + (3 * 5) - 8
result_2 = (5 + 3) * 2 - (12 / 4) + 7**2
result_3 = 10**0 - 1 == 1 and 1 == 1 and True

print("Result 1:", result_1)  # 29
print("Result 2:", result_2)  # 62
print("Result 3:", result_3)  # False

# Understood the operator precedence
# parentheses > exponentiation > multiplication/division
# > addition/subtraction > comparison > logical AND > logical OR
