def vieta_sum_of_roots(coefficients: list[float]) -> float:
    if len(coefficients) < 2:
        return 0
    return -coefficients[-2] / coefficients[-1]
