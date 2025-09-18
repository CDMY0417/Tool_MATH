def evaluate_polynomial(coefficients: list[int], x: int) -> int:
    return sum(c * (x ** i) for i, c in enumerate(coefficients))
