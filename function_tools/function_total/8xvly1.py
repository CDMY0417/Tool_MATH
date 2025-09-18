def gcd_using_prime_factors(factors1: dict, factors2: dict) -> int:
    gcd_factors = {}
    for p in factors1.keys() & factors2.keys():
        gcd_factors[p] = min(factors1[p], factors2[p])
    gcd = 1
    for p, exp in gcd_factors.items():
        gcd *= p ** exp
    return gcd
