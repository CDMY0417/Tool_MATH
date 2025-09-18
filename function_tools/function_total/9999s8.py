def simplify_fraction(numerator: int, denominator: int) -> tuple:
    import math
    gcd = math.gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)
