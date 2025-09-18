from fractions import Fraction

def convert_to_common_fraction(value: float):
    return Fraction(value).limit_denominator()
