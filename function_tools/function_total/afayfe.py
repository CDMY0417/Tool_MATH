def smallest_int_greater_than(value: float) -> int:
    return int(value) + 1 if value != int(value) else int(value + 1)
