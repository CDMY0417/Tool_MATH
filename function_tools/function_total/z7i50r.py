def prime_factorize(n: int) -> dict:
    factors = {}
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            if d not in factors:
                factors[d] = 0
            factors[d] += 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = 1
    return factors
