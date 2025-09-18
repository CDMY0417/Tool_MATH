def factor_product(n: int):
    factors = []
    for i in range(1, int(abs(n)**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
            if i != n // i:
                factors.append((n // i, i))
    return factors
