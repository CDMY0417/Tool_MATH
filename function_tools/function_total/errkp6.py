def is_power_of_two(x: int) -> bool:
    return x > 0 and (x & (x - 1)) == 0
