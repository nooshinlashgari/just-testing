def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y


# Example usage:
print("Addition: ", add(5, 3))
print("Addition: ", add(6, 9))
print("Subtraction: ", subtract(5, 3))
print("Multiplication: ", multiply(5, 3))
print("Division: ", divide(5, 0))  # Will show an error for division by zero
