def largest_power_less_than(base: int, num: int):
    power = 1
    exponent = 0
    while power * base <= num:
        power *= base
        exponent += 1
    return power // base, exponent - 1
