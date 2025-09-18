from math import gcd

def simplify_fraction(numerator: int, denominator: int) -> tuple:
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
