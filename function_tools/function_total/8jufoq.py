from math import gcd
from functools import reduce
def gcd_of_list(numbers: list[int]) -> int:
    return reduce(gcd, numbers)
