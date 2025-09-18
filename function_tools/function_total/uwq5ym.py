def divisors(n: int) -> list:
    from functools import reduce
    return sorted(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
