def simplify_ratio(a: int, b: int) -> tuple:
    from math import gcd
    divisor = gcd(a, b)
    return (a // divisor, b // divisor)
