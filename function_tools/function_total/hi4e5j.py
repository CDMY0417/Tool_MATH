def largest_integer_less_than(value: float) -> int:
    return int(value) if value - int(value) == 0 else int(value) - 1
