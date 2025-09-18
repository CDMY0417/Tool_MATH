def next_multiple(start: int, divisor: int) -> int:
    remainder = start % divisor
    if remainder == 0:
        return start
    return start + divisor - remainder
