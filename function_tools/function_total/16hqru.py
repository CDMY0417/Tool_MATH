def rationalize_denominator(a: float, b: float, c: float, d: float, e: float):
    numerator = (a * d * e**0.5) + (b * c)
    denominator = c
    return numerator, denominator
