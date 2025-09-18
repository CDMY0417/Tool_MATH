def interval_overlap(interval1: tuple, interval2: tuple) -> tuple:
    lower_bound = max(interval1[0], interval2[0])
    upper_bound = min(interval1[1], interval2[1])
    return (lower_bound, upper_bound)
