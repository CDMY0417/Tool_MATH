def largest_multiple_less_than(base_power: int, number: int):
    multiplier = number // base_power
    return multiplier * base_power, multiplier
