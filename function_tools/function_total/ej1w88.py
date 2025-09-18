from math import gcd

def simplify_vector_ratio(ratio: tuple[int, int]) -> tuple[int, int]:
    a, b = ratio
    b = -b
    gcd_ab = gcd(abs(a), abs(b))
    a //= gcd_ab
    b //= gcd_ab
    if a < 0:
        a = -a
        b = -b
    return a, b
