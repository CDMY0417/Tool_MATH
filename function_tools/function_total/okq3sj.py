def evaluate_polynomial(coefficients: list[float], x: float) -> float:
    a, b, c, d, e = coefficients
    return a * x**4 + b * x**3 + c * x**2 + d * x + e
