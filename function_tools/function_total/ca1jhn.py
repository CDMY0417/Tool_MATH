def gcd_of_prime_factorizations(factorization1: dict, factorization2: dict) -> dict:
    common_primes = set(factorization1.keys()).intersection(factorization2.keys())
    gcd_factors = {prime: min(factorization1[prime], factorization2[prime]) for prime in common_primes}
    return gcd_factors
