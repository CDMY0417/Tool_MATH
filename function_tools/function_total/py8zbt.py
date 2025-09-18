def product_of_powers(bases: list[float], powers: list[float]) -> float:
    product = 1
    for base, power in zip(bases, powers):
        product *= base ** power
    return product
