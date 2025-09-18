def count_divisors(factors: dict) -> int:
    count = 1
    for _, exponent in factors.items():
        count *= (exponent + 1)
    return count
