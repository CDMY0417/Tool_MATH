def prime_factors(n: int):
    i = 2
    factors = {}
    while i * i <= n:
        while (n % i) == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = 1
    return factors
