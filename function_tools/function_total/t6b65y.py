def evaluate_polynomial_at(coefficients: list[int], x: int) -> int:
    result = 0
    for i, coeff in enumerate(coefficients):
        result += coeff * (x ** i)
    return result
