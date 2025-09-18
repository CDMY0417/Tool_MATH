def evaluate_polynomial_at_point(coeffs: list[float], x: float) -> float:
    result = 0
    degree = len(coeffs) - 1
    for i in range(degree + 1):
        result += coeffs[i] * (x ** (degree - i))
    return result
