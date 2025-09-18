import math


def greatest_common_divisor(numbers: list[int]) -> int:
    if not numbers:
        return 0
    return math.gcd(*numbers)
