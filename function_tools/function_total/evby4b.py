def geometric_series_sum(a: float, r: float, n: int) -> float:
    return a * (1 - r**n) / (1 - r)
