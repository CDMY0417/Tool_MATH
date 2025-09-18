def modular_inverse(a: int, mod: int):
    for n in range(mod):
        if (a * n) % mod == 1:
            return n
    return None
