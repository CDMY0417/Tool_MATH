def floor_value(x: float) -> int:
    return int(x) if x >= 0 or x == int(x) else int(x) - 1
