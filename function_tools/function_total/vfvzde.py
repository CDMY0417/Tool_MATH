def largest_power_less_than(base: int, num: int) -> int:
    power = 0
    while base ** (power + 1) <= num:
        power += 1
    return power
