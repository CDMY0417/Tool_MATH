def sum_of_roots(coefficients: list[float]) -> float:
    degree = len(coefficients) - 1
    return -coefficients[-2] / coefficients[-1] if degree > 0 else 0
