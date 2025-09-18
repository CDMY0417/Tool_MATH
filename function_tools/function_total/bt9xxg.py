def relatively_prime_count(n: int, limit: int) -> int:
    from math import gcd
    return len([i for i in range(1, limit + 1) if gcd(i, n) == 1])
