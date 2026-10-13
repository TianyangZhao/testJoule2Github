"""Arithmetic tool for basic number operations."""

from langchain_core.tools import tool


@tool
def arithmetic(operation: str, a: float, b: float) -> str:
    """Perform a basic arithmetic operation between two numbers.

    Args:
        operation: One of 'add', 'subtract', 'multiply', 'divide', 'power', 'modulo'
        a: First number
        b: Second number

    Returns:
        Result as a string with description.
    """
    operation = operation.strip().lower()

    if operation == "add":
        result = a + b
        return f"{a} + {b} = {result}"
    elif operation == "subtract":
        result = a - b
        return f"{a} - {b} = {result}"
    elif operation == "multiply":
        result = a * b
        return f"{a} × {b} = {result}"
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero is undefined."
        result = a / b
        return f"{a} ÷ {b} = {result}"
    elif operation == "power":
        result = a ** b
        return f"{a} ^ {b} = {result}"
    elif operation == "modulo":
        if b == 0:
            return "Error: Modulo by zero is undefined."
        result = a % b
        return f"{a} mod {b} = {result}"
    else:
        return (
            f"Error: Unknown operation '{operation}'. "
            "Supported: add, subtract, multiply, divide, power, modulo."
        )
