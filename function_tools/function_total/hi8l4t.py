def is_perfect_sixth_power(n: int) -> bool:
    k = int(n ** (1/6))
    return k ** 6 == n
