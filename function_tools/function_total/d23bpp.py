def evaluate_polynomial(coefficients: tuple, variable: int) -> int:
    a2, a1, a0 = coefficients
    return a2 * variable**2 + a1 * variable + a0
