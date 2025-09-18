def evaluate_polynomial(coefficients: list[float], x: float) -> float:
    return sum(coef * (x ** i) for i, coef in enumerate(coefficients))
