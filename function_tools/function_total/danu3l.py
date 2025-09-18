def modular_inverse(b: int, m: int) -> int:
    for x in range(1, m):
        if (b * x) % m == 1:
            return x
    return None
