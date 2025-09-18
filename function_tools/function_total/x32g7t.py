def modular_exponentiation(base: int, exponent: int, mod: int) -> int:
    result = 1
    base = base % mod
    while exponent > 0:
        if (exponent % 2) == 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result
