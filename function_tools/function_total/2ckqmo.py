def count_multiples(multiple: int, start: int, end: int) -> int:
    return end // multiple - (start - 1) // multiple
