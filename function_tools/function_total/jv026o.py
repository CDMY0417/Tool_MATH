def evaluate_polynomial_at_value(coefficients: list[float], x: float) -> float:
    return sum(c * x ** i for i, c in enumerate(coefficients))
