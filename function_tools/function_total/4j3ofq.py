def evaluate_polynomial(x: int, coefficients: list[int]) -> int:
    result = 0
    for degree, coefficient in enumerate(coefficients):
        result += coefficient * (x ** degree)
    return result
