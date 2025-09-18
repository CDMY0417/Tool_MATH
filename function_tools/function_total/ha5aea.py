def count_perfect_squares(start: float, end: float) -> int:
    from math import ceil, floor
    return max(0, floor(end**0.5) - ceil(start**0.5) + 1)
