def union_of_intervals(interval1: tuple, interval2: tuple):
    return (min(interval1[0], interval2[0]), max(interval1[1], interval2[1]))
