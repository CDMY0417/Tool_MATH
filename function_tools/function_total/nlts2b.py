def gcd_from_prime_factors(factors_a: dict[int, int], factors_b: dict[int, int]) -> int:
    gcd_factors = {}
    for p in factors_a:
        if p in factors_b:
            gcd_factors[p] = min(factors_a[p], factors_b[p])
    gcd_value = 1
    for p, power in gcd_factors.items():
        gcd_value *= p ** power
    return gcd_value
