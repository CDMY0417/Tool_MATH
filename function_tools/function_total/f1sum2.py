def count_perfect_square_factors(prime_exponents: list[int]) -> int:
    count = 1
    for exp in prime_exponents:
        count *= (exp // 2 + 1)
    return count
