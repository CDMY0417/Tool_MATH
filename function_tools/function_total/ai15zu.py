def evaluate_polynomial(coefficients: list[int], x: int) -> int:
    return sum(coefficient * (x ** i) for i, coefficient in enumerate(coefficients))
