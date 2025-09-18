def floor_of_number(value: float) -> int:
    return int(value) if value >= 0 or value == int(value) else int(value) - 1
