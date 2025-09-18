def evaluate_polynomial(coefficients: list[int], x_value: int) -> int:
    degree = len(coefficients) - 1
    result = 0
    for coeff in coefficients:
        result = result * x_value + coeff
    return result
