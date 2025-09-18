def greatest_common_divisor(numbers: list[int]) -> int:
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)
