def generate_zero_sum_pairs(n: int):
    pairs = []
    for i in range(1, n // 2 + 1):
        pairs.append((i, n - i))
    if n % 2 == 0:
        pairs.append((n // 2, n // 2))
    return pairs
