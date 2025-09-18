from fractions import Fraction

def fraction_as_common_fraction(numerator: int, denominator: int) -> str:
    return str(Fraction(numerator, denominator))
