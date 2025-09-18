def poly_eval(x: float, coefficients: list[float]) -> float:
    result = 0
    degree = len(coefficients) - 1
    for i, coef in enumerate(coefficients):
        result += coef * (x ** (degree - i))
    return result
