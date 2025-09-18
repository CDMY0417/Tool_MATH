def first_multiple_in_range(multiple: int, start: int) -> int:
    if start % multiple == 0:
        return start
    else:
        return (start // multiple + 1) * multiple
