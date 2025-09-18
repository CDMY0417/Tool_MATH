def least_common_multiple(a: int, b: int) -> int:
    import math
    return abs(a * b) // math.gcd(a, b)
