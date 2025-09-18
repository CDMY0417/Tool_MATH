def count_integer_squares_in_range_exclusive(lo: int, hi: int) -> int:
    count = int(hi**0.5) - int(lo**0.5)
    return count
