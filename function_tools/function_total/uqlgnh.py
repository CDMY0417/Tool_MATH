import math

def reduce_fraction(numerator: int, denominator: int):
    gcd = math.gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)
