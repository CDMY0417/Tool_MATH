def multiply_equation(coefficients: tuple, constant: float, scalar: float):
    return tuple(scalar * c for c in coefficients), scalar * constant
