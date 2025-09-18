def evaluate_polynomial(coefficients: list[float], x: float) -> float:
    result = sum(c * (x ** i) for i, c in enumerate(coefficients))
    return result
