def law_of_cosines(a: float, b: float, c: float) -> float:
    cos_gamma = (a**2 + b**2 - c**2) / (2 * a * b)
    return cos_gamma
