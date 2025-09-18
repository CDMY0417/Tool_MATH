from math import gcd
from functools import reduce
def greatest_common_factor(numbers: list[int]) -> int:
    return reduce(gcd, numbers)
