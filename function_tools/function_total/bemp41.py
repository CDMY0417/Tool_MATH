def is_perfect_square(num: int) -> bool:
    root = int(num**0.5)
    return num == root * root
