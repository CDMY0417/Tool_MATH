def expand_cubic_factors(a1: int, a2: int, a3: int):
    c3 = -a1 * a2 * a3
    c2 = a1 * a2 + a1 * a3 + a2 * a3
    c1 = -(a1 + a2 + a3)
    c0 = 1
    return c3, c2, c1, c0
