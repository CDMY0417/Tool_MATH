def count_divisors(prime_factors: dict) -> int:
    count = 1
    for exponent in prime_factors.values():
        count *= (exponent + 1)
    return count
