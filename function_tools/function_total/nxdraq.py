def simplify_polynomial(coefficients: list[int]) -> list[int]:
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients
