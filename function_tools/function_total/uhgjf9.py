def prime_factorization(number: int) -> dict:
    factors = {}
    divisor = 2
    while number >= 2:
        while number % divisor == 0:
            if divisor in factors:
                factors[divisor] += 1
            else:
                factors[divisor] = 1
            number //= divisor
        divisor += 1
    return factors
