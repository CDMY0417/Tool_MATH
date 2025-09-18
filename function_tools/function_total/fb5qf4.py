def modular_inverse(a: int, mod: int) -> int:
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    return None
