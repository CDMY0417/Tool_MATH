def proper_divisors(n: int) -> set:
    divisors = set()
    for i in range(1, n):
        if n % i == 0:
            divisors.add(i)
    return divisors
