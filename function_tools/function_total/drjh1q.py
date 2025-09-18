def find_interval_intersection(interval1: tuple[float, float], interval2: tuple[float, float]):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start >= end:
        return None
    return (start, end)
