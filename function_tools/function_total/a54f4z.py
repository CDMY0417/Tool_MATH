def count_perfect_square_factors(exponents: list[int]) -> int:
    count = 1
    for max_exp in exponents:
        count *= (max_exp // 2 + 1)
    return count
