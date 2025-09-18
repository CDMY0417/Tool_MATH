def count_multiples_in_range(n: int, start: int, end: int) -> int:
    return (end // n) - ((start - 1) // n)
