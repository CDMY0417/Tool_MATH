from fractions import Fraction
from typing import Tuple

def multiply_fractions(fractions: list[Tuple[int, int]]) -> Tuple[int, int]:
    result = Fraction(1, 1)
    for numerator, denominator in fractions:
        result *= Fraction(numerator, denominator)
    return result.numerator, result.denominator
