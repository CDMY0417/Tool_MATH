def count_combinations(option_counts: list[int]) -> int:
    from functools import reduce
    from operator import mul
    return reduce(mul, option_counts, 1)
