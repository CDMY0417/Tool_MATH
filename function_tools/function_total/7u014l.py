def intersection_of_intervals(interval1: tuple[float, float], interval2: tuple[float, float]) -> tuple[float, float]:
    a, b = interval1
    c, d = interval2
    return (max(a, c), min(b, d))
