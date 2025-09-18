def find_pair_for_sum(target_sum: int, upper_bound: int) -> list:
    pairs = []
    for i in range(1, upper_bound):
        j = target_sum - i
        if i < j < upper_bound:
            pairs.append((i, j))
    return pairs
