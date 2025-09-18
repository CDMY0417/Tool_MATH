def stewarts_theorem_median(a: float, b: float, c: float) -> float:
    m = c / 2
    return ((2 * b**2 + 2 * a**2 - c**2) / 4) ** 0.5
