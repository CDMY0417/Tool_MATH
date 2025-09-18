def evaluate_polynomial(coefficients: list[int], x: int) -> int:
    return sum(coef * (x ** i) for i, coef in enumerate(coefficients[::-1]))
