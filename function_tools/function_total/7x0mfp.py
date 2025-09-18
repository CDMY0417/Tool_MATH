def least_common_denominator(den1: int, den2: int) -> int:
    from math import gcd
    return abs(den1 * den2) // gcd(den1, den2)
