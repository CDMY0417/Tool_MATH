def generate_sums(elements: list[int]) -> set:
    from itertools import combinations_with_replacement
    sums = set(sum(comb) for comb in combinations_with_replacement(elements, 3))
    return sums
