def rationalize_denominator(numerator: float, a: float, b: float, c: float) -> float:
    denominator = a**2 - (b**2) * c
    return numerator * (a - b * c**0.5) / denominator
