def simplify_radical(factors: dict):
    outside = 1
    inside = 1
    for prime, exponent in factors.items():
        outside *= (prime ** (exponent // 2))
        if exponent % 2 != 0:
            inside *= prime
    return outside, inside
