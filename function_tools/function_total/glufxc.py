def number_of_divisors(exponents: list[int]) -> int:
    result = 1
    for exp in exponents:
        result *= (exp + 1)
    return result
