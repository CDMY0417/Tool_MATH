def geometric_series_sum(a: int, r: int, n: int) -> int:
    return a * (1 - r**n) // (1 - r)
