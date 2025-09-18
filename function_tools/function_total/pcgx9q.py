def is_divisible_by_7(n: int) -> bool:
    while n >= 10:
        n = n // 10 - 2 * (n % 10)
    return n in {0, 7}
