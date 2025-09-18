def evaluate_polynomial(coefficients: list[int], x_value: int) -> int:
    return sum(coef * (x_value ** i) for i, coef in enumerate(coefficients))
