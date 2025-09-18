def largest_multiple_of_power_less_than(base: int, power: int, number: int) -> int:
    power_value = base ** power
    multiple = number // power_value
    return multiple * power_value
