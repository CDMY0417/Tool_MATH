def largest_multiple_less_than(n: int, limit: int) -> int:
    k = (limit - 1) // n
    return k * n
