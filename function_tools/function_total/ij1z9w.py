def calculate_probability(count: int, total: int):
    from fractions import Fraction
    return Fraction(count, total)
