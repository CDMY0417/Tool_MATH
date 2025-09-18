def pair_products(numbers: list[int]) -> list[int]:
    from itertools import combinations
    return [a * b for a, b in combinations(numbers, 2)]
