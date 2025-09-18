def ceil_value(value: float) -> int:
    return int(value) + 1 if value - int(value) > 0 else int(value)
