"""Functions to evaluate infix expressions and converting to postfix."""

# Constants
DIGITS = "0123456789"
ERROR_DIVISION_BY_ZERO = "Division by zero is not allowed."
ERROR_INVALID_CHAR = (
    "Invalid expression the expression should contain only "
    '`0123456789+-*/^()`, but found "{char}"'
)
ERROR_INVALID_EXPRESSION_SYNTAX = "Invalid expression syntax"
ERROR_MISMATCHED_PARENTHESES = "Mismatched parentheses"
ERROR_UNKNOWN_OPERATOR = "Unknown operator: {operator}"
INPUT_PROMPT = "Enter a valid expression `0123456789+-*/^()`: \n"
INTERRUPT_MESSAGE = "Program interrupted by the user, shutting down!"
UNEXPECTED_ERROR = "Unexpected error: {error}"
VALID_CHARS = "0123456789+-*/^()"


def get_operator_precedence(operator: str) -> int:
    """Find the precedence of the operator.

    Args:
        operator : Operator for which the precedence is needed.

    Returns:
        Precedence of the operator passed.
    """
    precedences = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    return precedences.get(operator, 0)


def evaluate_simple_expression(operand_a: float, operand_b: float, operator: str) -> float:
    """Evaluate the simple expression with two operand.

    Args:
        operand_a : First operand.
        operand_b : Second operand.
        operator : Operator.

    Raises:
        ValueError: If the operator is unknown.

    Returns:
        Result of the expression.
    """
    if operator == "+":
        return operand_a + operand_b
    elif operator == "-":
        return operand_a - operand_b
    elif operator == "*":
        return operand_a * operand_b
    elif operator == "/":
        return operand_a / operand_b
    elif operator == "^":
        return operand_a**operand_b
    else:
        raise ValueError(ERROR_UNKNOWN_OPERATOR.format(operator=operator))


def get_postfix_expression(expression: str) -> list[str]:
    """Convert an infix expression to postfix expression.

    Args:
        expression : Infix expression to be converted to postfix.

    Raises:
        ValueError : Raised if the character of the expression is invalid.

    Returns:
        Postfix expression as a list.
    """
    stack: list[str] = []
    number = ""
    postfix_expression: list[str] = []

    for char in expression:
        if char not in VALID_CHARS:
            raise ValueError(ERROR_INVALID_CHAR.format(char=char))

        if char in DIGITS:
            number += char
            continue

        if number:
            postfix_expression.append(number)
            number = ""

        if char == "(":
            stack.append(char)

        elif char == ")":
            if "(" not in stack:
                raise ValueError(ERROR_MISMATCHED_PARENTHESES)

            while stack and stack[-1] != "(":
                postfix_expression.append(stack.pop())
            stack.pop()

        else:
            precedence = get_operator_precedence(char)
            while stack and stack[-1] != "(" and get_operator_precedence(stack[-1]) >= precedence:
                postfix_expression.append(stack.pop())
            stack.append(char)

    if number:
        postfix_expression.append(number)

    while stack:
        op = stack.pop()
        if op == "(":
            raise ValueError(ERROR_MISMATCHED_PARENTHESES)
        postfix_expression.append(op)

    return postfix_expression


def evaluate_expression(expression: str) -> float:
    """Evaluate the infix expression.

    Args:
        expression : Infix expression to be evaluated.

    Raises:
        ValueError: If the expression is invalid.
        ZeroDivisionError: If division by zero is attempted.

    Returns:
        Final value of the expression.
    """
    expression = expression.replace(" ", "")
    postfix = get_postfix_expression(expression)

    try:
        stack: list[float] = []

        for token in postfix:
            if token.isdigit():
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(evaluate_simple_expression(a, b, token))

        if len(stack) != 1:
            raise ValueError(ERROR_INVALID_EXPRESSION_SYNTAX)

        return stack.pop()

    except IndexError:
        raise ValueError(ERROR_INVALID_EXPRESSION_SYNTAX)


if __name__ == "__main__":
    try:
        expression = input(INPUT_PROMPT)
        print(evaluate_expression(expression))

    except KeyboardInterrupt:
        print(INTERRUPT_MESSAGE)

    except ValueError as ve:
        print(f"Error: {ve}")

    except ZeroDivisionError:
        print(f"Error: {ERROR_DIVISION_BY_ZERO}")

    except Exception as e:
        print(UNEXPECTED_ERROR.format(error=e))
