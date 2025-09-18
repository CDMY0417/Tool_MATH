def perfect_square_check(prime_factors: dict) -> bool:
    return all(exponent % 2 == 0 for exponent in prime_factors.values())
