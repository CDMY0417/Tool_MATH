def geometric_series_sum(a: int, n: int) -> int:
    return (a ** (n + 1) - 1) // (a - 1)
