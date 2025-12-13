"""Utilities for evaluating infix expressions and converting to postfix."""

from typing import List


def operator_precedence(op: str) -> int:
    """To find the precedence of the operator.

    Args:
        op (str): Operator or parenthesis

    Returns:
        int: precedence value
    """
    precedences = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    return precedences.get(op, 0)


def evaluate_simple_expression(
    operand1: float,
    operand2: float,
    operator: str,
) -> float:
    """To evaluate the simple expression with two operand.

    Args:
        operand1 (float): Operand_1
        operand2 (float): Operand_2
        operator (str): Operator

    Raises:
        ValueError: if the operator is unknown
        ZeroDivisionError: if division by zero is attempted

    Returns:
        float: Result of the expression
    """
    try:
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            return operand1 / operand2
        elif operator == "^":
            return operand1**operand2
        else:
            raise ValueError(f"Unknown operator: {operator}")
    except ZeroDivisionError:
        raise


def postfix_conversion(expression: str) -> List[str]:
    """To convert the infix expression to post-fix expression.

    Args:
        expression (str): Infix expression

    Raises:
        ValueError: Raised if the character of the expression is invalid

    Returns:
        List[str]: post-fix expression as a list
    """
    stack: List[str] = []
    postfix_expression: List[str] = []
    for char in expression:
        if char not in "0123456789+-*/^()":
            raise ValueError(f"Invalid: {char}")
        number = ""
        if char in "0123456789":
            number += char
            while len(expression) > 1 and expression[1] in "0123456789":
                number += expression[1]
                expression = expression[1:]
            postfix_expression.append(number)
        elif char == ")":
            while stack and stack[-1] != "(":
                postfix_expression.append(stack.pop())
            stack.pop()
            idx = expression.index(")")
            expression = expression[idx + 1 :]
        elif char == "(":
            stack.append(char)
            expression = expression[1:]
        else:
            precedence = operator_precedence(char)
            while stack and operator_precedence(stack[-1]) >= precedence:
                postfix_expression.append(stack.pop())
            stack.append(char)

    while stack:
        postfix_expression.append(stack.pop())

    return postfix_expression


def expression_evaluator(expression: str) -> float:
    """To evaluate the infix expression.

    Args:
        expression (str): Infix expression

    Raises:
        ValueError: if the expression is invalid
        ZeroDivisionError: if division by zero is attempted

    Returns:
        float: value of the expression
    """
    expression.replace(" ", "")
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
