def reduce_fraction(num: int, denom: int):
    from math import gcd
    common_divisor = gcd(num, denom)
    return num // common_divisor, denom // common_divisor
