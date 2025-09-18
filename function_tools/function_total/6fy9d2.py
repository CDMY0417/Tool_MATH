def compute_ratio(sum_a: float, sum_b: float):
    from fractions import Fraction
    fraction = Fraction(sum_a, sum_b)
    return fraction.numerator, fraction.denominator
