"""Module for evaluating infix expressions and converting to postfix."""

from typing import List


def operator_precedence(operator: str) -> int:
    """To find the precedence of the operator.

    Args:
        operator : Operator for which the precedence is needed.

    Returns:
        Precedence of the operator passed.
    """
    precedences = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    return precedences.get(operator, 0)


def evaluate_simple_expression(operand_1: float, operand_2: float, operator: str) -> float:
    """Evaluates the simple expression with two operand.

    Args:
        operand_1 : First operand.
        operand_2 : Second operand.
        operator : Operator.

    Raises:
        ValueError: If the operator is unknown.
        ZeroDivisionError: If division by zero is attempted.

    Returns:
        Result of the expression.
    """
    try:
        if operator == "+":
            return operand_1 + operand_2
        elif operator == "-":
            return operand_1 - operand_2
        elif operator == "*":
            return operand_1 * operand_2
        elif operator == "/":
            return operand_1 / operand_2
        elif operator == "^":
            return operand_1**operand_2
        else:
            raise ValueError(f"Unknown operator: {operator}")
    except ZeroDivisionError:
        raise


def postfix_conversion(expression: str) -> List[str]:
    """Converts an infix expression to postfix expression.

    Args:
        expression : Infix expression to be converted to postfix.

    Raises:
        ValueError : Raised if the character of the expression is invalid.

    Returns:
        Postfix expression as a list.
    """
    stack: List[str] = []
    number = ""
    postfix_expression: List[str] = []
    for char in expression:
        if char not in "0123456789+-*/^()":
            raise ValueError(f"Invalid: {char}")
        if char in "0123456789":
            number += char
            continue
        if number != "":
            postfix_expression.append(number)
            number = ""
        if char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                postfix_expression.append(stack.pop())
            stack.pop()
            expression = expression[expression.index(")") + 1 :]
        else:
            precedence = operator_precedence(char)
            while stack and operator_precedence(stack[-1]) > precedence:
                postfix_expression.append(stack.pop())
            stack.append(char)
    if number != "":
        postfix_expression.append(number)
    while stack:
        postfix_expression.append(stack.pop())

    return postfix_expression


def expression_evaluator(expression: str) -> float:
    """Evaluates the infix expression.

    Args:
        expression : Infix expression to be evaluated.

    Raises:
        ValueError: If the expression is invalid.
        ZeroDivisionError: If division by zero is attempted.

    Returns:
        Final value of the expression.
    """
    expression = expression.replace(" ", "")
    postfix: List[str]
    try:
        postfix = postfix_conversion(expression)
    except ValueError:
        raise

    try:
        stack: List[float] = []
        for token in postfix:
            if token.isdigit():
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = evaluate_simple_expression(a, b, token)
                stack.append(result)

        return stack.pop()
    except ValueError:
        raise
    except ZeroDivisionError:
        raise


if __name__ == "__main__":
    expression = input("Enter the expression: ")
    try:
        print(expression_evaluator(expression))
    except ValueError as ve:
        print(f"Error: {ve}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
