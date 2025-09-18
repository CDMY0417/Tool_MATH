def prime_factorization(n: int):
    factors = {}
    div = 2
    while n > 1:
        count = 0
        while n % div == 0:
            n //= div
            count += 1
        if count > 0:
            factors[div] = count
        div += 1
    return factors
