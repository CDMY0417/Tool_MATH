def polynomial_evaluation(coefficients: list[float], x: float) -> float:
    result = 0
    for i, coeff in enumerate(coefficients):
        result += coeff * (x ** i)
    return result
