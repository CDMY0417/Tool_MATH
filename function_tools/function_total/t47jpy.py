def greatest_common_factor(numbers: list[int]) -> int:
    from functools import reduce
    from math import gcd
    return reduce(gcd, numbers)
