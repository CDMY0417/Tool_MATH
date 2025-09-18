from fractions import Fraction

def calculate_ratio(numerator: float, denominator: float) -> Fraction:
    return Fraction(numerator, denominator).limit_denominator()
