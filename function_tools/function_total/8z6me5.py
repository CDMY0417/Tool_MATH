from fractions import Fraction

def add_fractions(fraction1: tuple[int, int], fraction2: tuple[int, int]):
    frac1 = Fraction(fraction1[0], fraction1[1])
    frac2 = Fraction(fraction2[0], fraction2[1])
    return frac1 + frac2
