def is_terminating_decimal(a: int, b: int) -> bool:
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    return b == 1
