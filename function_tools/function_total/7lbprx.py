def least_common_multiple(a: int, b: int) -> int:
    from math import gcd
    return (a * b) // gcd(a, b)
