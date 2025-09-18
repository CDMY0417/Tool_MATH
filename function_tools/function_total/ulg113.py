def factorize_integer(n: int):
    factors = []
    divisor = 2
    abs_n = abs(n)
    while abs_n >= 2:
        while abs_n % divisor == 0:
            factors.append(divisor)
            abs_n //= divisor
        divisor += 1
        if divisor * divisor > abs_n > 1:
            factors.append(abs_n)
            break
    if n < 0:
        factors += [-f for f in factors.copy()]
        factors.append(-1)
    return factors
