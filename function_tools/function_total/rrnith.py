def is_coprime(a: int, b: int, c: int) -> bool:
    from math import gcd
    return gcd(abs(a), abs(b), abs(c)) == 1
