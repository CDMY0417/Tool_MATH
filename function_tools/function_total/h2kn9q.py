def count_multiples_in_range(start: int, end: int, divisor: int) -> int:
    return end // divisor - (start - 1) // divisor
