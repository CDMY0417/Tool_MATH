def integer_points_in_open_interval(lo: int, hi: int) -> int:
    if lo >= hi:
        return 0
    return hi - lo - 1
