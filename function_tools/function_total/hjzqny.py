def least_common_denominator(d1: int, d2: int) -> int:
    from math import gcd
    return d1 * d2 // gcd(d1, d2)
