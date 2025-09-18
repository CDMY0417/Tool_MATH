def evaluate_polynomial(coeffs: list[float], x: float) -> float:
    result = 0
    degree = len(coeffs) - 1
    for coeff in coeffs:
        result += coeff * (x ** degree)
        degree -= 1
    return result
