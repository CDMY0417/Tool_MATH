from itertools import combinations
from typing import Tuple

def distinct_groupings_of_factors(factors: list[int]) -> list[Tuple[int, int]]:
    def combine_subgroup(subgroup):
        product = 1
        for num in subgroup:
            product *= num
        return product

    unique_groupings = []
    for i in range(1, len(factors)):
        for combo in combinations(factors, i):
            rest = list(factors)
            for num in combo:
                rest.remove(num)
            unique_groupings.append((combine_subgroup(combo), combine_subgroup(rest)))
    return unique_groupings
