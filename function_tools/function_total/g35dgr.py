def count_divisors(exponents: list[int]) -> int:
    count = 1
    for e in exponents:
        count *= (e + 1)
    return count
