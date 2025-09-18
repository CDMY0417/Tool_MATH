def power_ratio_series_sum(a: float, b: float, start: int, end: int) -> float:
    return a / (b ** start) * (1 - (b ** (end - start + 1))) / (1 - 1/b)
