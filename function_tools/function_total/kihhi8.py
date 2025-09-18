def count_multiples_in_range(k: int, lo: int, hi: int) -> int:
    return hi // k - (lo - 1) // k
