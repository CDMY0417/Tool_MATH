def count_integers_with_offset_multiple(multiple: int, offset: int, start: int, end: int) -> int:
    first = (start + multiple - offset) // multiple * multiple + offset
    if first > end:
        return 0
    return (end - first) // multiple + 1
