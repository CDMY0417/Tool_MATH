def vieta_sum_of_roots(coefficients: list[float]) -> float:
    n = len(coefficients)
    if n < 2:
        return 0.0
    return -coefficients[n-2] / coefficients[n-1]
