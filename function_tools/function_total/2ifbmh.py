def simplify_fraction(numerator: int, denominator: int) -> tuple:
    from math import gcd
    factor = gcd(numerator, denominator)
    return (numerator // factor, denominator // factor)
