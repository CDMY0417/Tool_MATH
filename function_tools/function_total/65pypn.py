def proper_divisors(n: int) -> list:
    return [i for i in range(1, n) if n % i == 0]
