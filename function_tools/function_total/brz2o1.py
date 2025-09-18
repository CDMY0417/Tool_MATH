def factor_pairs(product: int):
    pairs = []
    for i in range(1, int(product**0.5) + 1):
        if product % i == 0:
            pairs.append((i, product // i))
    return pairs
