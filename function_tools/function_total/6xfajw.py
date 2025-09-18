def evaluate_polynomial_at_value(coefficients: list, x_value: int):
    return sum(coef * (x_value ** i) for i, coef in enumerate(coefficients))
