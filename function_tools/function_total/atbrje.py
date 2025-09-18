def is_invertible_modulo(x: int, n: int) -> bool:
    import math
    return math.gcd(x, n) == 1
