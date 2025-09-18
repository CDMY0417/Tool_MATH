from math import gcd

def greatest_common_divisor(a: int, b: int, c: int):
    return gcd(gcd(a, b), c)
