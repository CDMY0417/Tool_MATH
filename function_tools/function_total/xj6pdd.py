from math import gcd

def simplify_fraction(numerator: int, denominator: int):
    factor = gcd(numerator, denominator)
    return (numerator // factor, denominator // factor)
