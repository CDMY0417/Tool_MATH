def evaluate_polynomial_at_point(coefficients: list[int], x: int) -> int:
    result = 0
    for power, coefficient in enumerate(coefficients):
        result += coefficient * (x ** power)
    return result
