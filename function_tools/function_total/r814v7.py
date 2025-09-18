from itertools import combinations

def combinations_with_sum(n: int, k: int, target: int):
    return [combo for combo in combinations(range(1, n+1), k) if sum(combo) == target]
