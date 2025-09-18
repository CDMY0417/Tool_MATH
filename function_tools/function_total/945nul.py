def simplify_fraction(a: int, b: int) -> tuple:
    import math
    gcd = math.gcd(a, b)
    return (a // gcd, b // gcd)
