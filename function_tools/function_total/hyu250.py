def simplify_ratio(numerator: int, denominator: int) -> tuple:
    from math import gcd
    divisor = gcd(numerator, denominator)
    return (numerator // divisor, denominator // divisor)
