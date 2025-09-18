def series_sum(start: int, end: int, n: int):
    total = 0
    for i in range(start, end + 1):
        total += (n + start - i) / i
    return total
