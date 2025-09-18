def evaluate_polynomial_sum_at(x: int, coefficients: list[int]) -> int:
    result = 0
    for i, coeff in enumerate(coefficients):
        result += coeff * ((x + 2) ** (len(coefficients) - i - 1))
    return result
