def integer_points_in_range(start: int, end: int, exceptions: set):
    return [i for i in range(start, end + 1) if i not in exceptions]
