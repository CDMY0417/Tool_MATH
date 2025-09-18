def multiply_equation(coefficients: tuple, result: int, scalar: int):
    return tuple(c * scalar for c in coefficients), result * scalar
