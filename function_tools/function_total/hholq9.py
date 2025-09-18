def gcd_of_list(numbers: list[int]):
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)
