def eval_polynomial_at_point(coefficients: list[float], x: float) -> float:
    result = 0
    degree = len(coefficients) - 1
    for coef in coefficients:
        result += coef * (x ** degree)
        degree -= 1
    return result
