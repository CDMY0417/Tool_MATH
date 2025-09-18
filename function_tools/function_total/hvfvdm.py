def largest_power_of_2_less_than(n: int) -> int:
    power = 1
    while power * 2 < n:
        power *= 2
    return power
