def combinations_count(n: int, k: int) -> int:
    if k > n:
        return 0
    from math import comb
    return comb(n, k)
