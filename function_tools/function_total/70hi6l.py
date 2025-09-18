def pairwise_product(factors: list[int]) -> list[int]:
    from itertools import combinations
    products = []
    for a, b in combinations(factors, 2):
        products.append(a * b)
    return products
