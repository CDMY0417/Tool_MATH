def sum_arithmetic_sequence(start: int, end: int, difference: int) -> int:
    n = ((end - start) // difference) + 1
    return n * (start + end) // 2
