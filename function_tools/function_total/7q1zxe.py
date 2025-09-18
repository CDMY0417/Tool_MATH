def product_of_factors(factors: list[int]) -> int:
    result = 1
    for factor in factors:
        result *= factor
    return result
