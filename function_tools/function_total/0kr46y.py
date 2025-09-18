def simplify_fraction(numerator: int, denominator: int) -> tuple:
    from math import gcd
    g = gcd(numerator, denominator)
    return (numerator // g, denominator // g)
