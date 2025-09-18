def count_combinations(group_sizes: list[int]) -> int:
    from functools import reduce
    from operator import mul
    return reduce(mul, group_sizes, 1)
