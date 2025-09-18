def simplify_fraction(numerator: int, denominator: int):
    from math import gcd
    gcd_val = gcd(numerator, denominator)
    return (numerator // gcd_val, denominator // gcd_val)
