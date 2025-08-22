def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.

    Args:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        float or str: The result, or an error message
    """
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"
