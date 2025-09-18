def greatest_common_factor(factors1: dict, factors2: dict) -> int:
    gcf = 1
    common_primes = set(factors1.keys()).intersection(factors2.keys())
    for prime in common_primes:
        gcf *= prime ** min(factors1[prime], factors2[prime])
    return gcf
