def count_divisors_multiple_of_prime(prime_factors: dict, multiple_prime: int) -> int:
    count = 1
    for prime, exponent in prime_factors.items():
        if prime == multiple_prime:
            count *= exponent
        else:
            count *= (exponent + 1)
    return count
