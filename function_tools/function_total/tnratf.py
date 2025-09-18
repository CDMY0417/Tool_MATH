def count_multiples_in_range(k: int, start: int, end: int) -> int:
    return (end // k) - ((start - 1) // k)
