def count_multiples_in_range(number: int, start: int, end: int) -> int:
    return (end // number) - ((start - 1) // number)
