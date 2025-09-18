def simplify_fraction_product(numerator_terms: list[int], denominator_terms: list[int]) -> float:
    from math import gcd
    num_product, denom_product = 1, 1
    for num, denom in zip(numerator_terms, denominator_terms):
        g = gcd(num, denom)
        num_product *= num // g
        denom_product *= denom // g
    return num_product / denom_product
