def least_common_denominator(denom1: int, denom2: int) -> int:
    from math import gcd
    return denom1 * denom2 // gcd(denom1, denom2)
