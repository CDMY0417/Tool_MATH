def find_common_interval(interval1: tuple, interval2: tuple):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    if start < end:
        return (start, end)
    else:
        return None
