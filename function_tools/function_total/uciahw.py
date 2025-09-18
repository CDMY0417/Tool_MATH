def multiply_prime_factors(prime_factors: dict, new_prime: int, new_exponent: int) -> dict:
    new_factors = prime_factors.copy()
    if new_prime in new_factors:
        new_factors[new_prime] += new_exponent
    else:
        new_factors[new_prime] = new_exponent
    return new_factors
