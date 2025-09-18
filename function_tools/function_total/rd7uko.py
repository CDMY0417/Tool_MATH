def is_defined_for_value(value: float, denominators: list[float]) -> bool:
    for denom in denominators:
        if value in denom:
            return False
    return True
