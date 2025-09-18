def multiply_equation(coefficients: list[int], constant: int, scalar: int):
    new_coeffs = [c * scalar for c in coefficients]
    new_constant = constant * scalar
    return new_coeffs, new_constant
