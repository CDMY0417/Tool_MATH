def fraction_difference(frac1: str, frac2: str):
    from fractions import Fraction
    result = Fraction(frac1) - Fraction(frac2)
    return result
