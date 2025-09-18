def modular_multiplicative_inverse(a: int, m: int):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return None
