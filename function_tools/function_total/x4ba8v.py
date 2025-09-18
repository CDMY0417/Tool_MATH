def total_combinations(choices_per_category: list[int]) -> int:
    from functools import reduce
    from operator import mul
    total = reduce(mul, choices_per_category, 1)
    return total
