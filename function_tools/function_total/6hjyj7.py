def factor_pairs(n: int):
    pairs = []
    for x in range(1, int(n**0.5) + 1):
        if n % x == 0:
            pairs.append((x, n // x))
    return pairs
