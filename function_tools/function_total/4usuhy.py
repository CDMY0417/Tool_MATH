def is_perfect_square(num: int) -> bool:
    if num < 0:
        return False
    return int(num ** 0.5) ** 2 == num
