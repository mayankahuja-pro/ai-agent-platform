from langchain_core.tools import tool


@tool
def calculate(
    operation: str,
    a: float,
    b: float,
) -> dict:
    """
    Perform a basic mathematical calculation.

    Supported operations:
    add, subtract, multiply, divide.
    """

    if operation == "add":

        result = a + b

    elif operation == "subtract":

        result = a - b

    elif operation == "multiply":

        result = a * b

    elif operation == "divide":

        if b == 0:

            return {
                "error": "Division by zero is not allowed."
            }

        result = a / b

    else:

        return {
            "error": (
                "Unsupported operation. "
                "Use add, subtract, multiply, "
                "or divide."
            )
        }

    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result,
    }