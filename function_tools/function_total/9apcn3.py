def count_multiples_in_range(multiple: int, start: int, end: int) -> int:
    return end // multiple - (start - 1) // multiple
