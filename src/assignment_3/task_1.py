import re
from typing import Any, List

def operator_precedence(op: str) -> int:
    precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '**': 3}
    return precedences.get(op, 0)

def evaluate_simple_expression(operand1: float, operand2: float, operator: str) -> float | None:
    try:
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        elif operator in ('^', '**'):
            return operand1 ** operand2
        else:
            raise ValueError(f"Unknown operator: {operator}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None

def postfix_conversion(expression : str = "") -> List[Any] | None:
    stack : List[str]= []
    postfix_exper : List[Any] = []
    for char in expression:
        if char not in "0123456789+-*/^":
            print(f"Error: Invalid character '{char}' in expression.")
            return None
        number =""

        if char in "0123456789":
            number += char
            while len(expression) > 1 and expression[1] in "0123456789":
                number += expression[1]
                expression = expression[1:]
            postfix_exper.append(number)
        else:
            precdence = operator_precedence(char)
            while(len(stack) > 0 and operator_precedence(stack[-1]) >= precdence):
                postfix_exper.append(stack.pop())
            stack.append(char)

    while len(stack) > 0:
        postfix_exper.append(stack.pop())

    return postfix_exper

def expression_evaluator(expression : str = ""):
    postfix = postfix_conversion(expression)
    if postfix is None:
        return None
    while len(postfix) > 0:
        for index,char in enumerate(postfix):
            if char in "+/*-^":
                temp = evaluate_simple_expression(postfix.pop(index - 2), postfix.pop(index - 1), char)
                print(postfix)
       
        

if __name__ == "__main__":
    print(expression_evaluator("3+5-2*8/4"))