def combine_fractions(a: int, b: int, c: int, d: int):
    numerator = a * d + b * c
    denominator = b * d
    return numerator, denominator
