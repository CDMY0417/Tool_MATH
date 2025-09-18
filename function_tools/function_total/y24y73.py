def calculate_product(factors: dict[int, int]) -> int:
    product = 1
    for base, exp in factors.items():
        product *= base ** exp
    return product
