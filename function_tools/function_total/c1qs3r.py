def evaluate_polynomial(coeffs: list[float], x: float) -> float:
    return sum(c * (x ** i) for i, c in enumerate(coeffs))
