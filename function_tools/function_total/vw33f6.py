def evaluate_polynomial(coefficients: list[float], x: float) -> float:
    result = 0
    for power, coeff in enumerate(coefficients):
        result += coeff * (x ** power)
    return result
