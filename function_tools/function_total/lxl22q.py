def product_from_factors(factors: dict[int, int]) -> int:
    product = 1
    for base, power in factors.items():
        product *= base ** power
    return product
