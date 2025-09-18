def is_perfect_square(num: int) -> bool:
    root = int(num ** 0.5)
    return root * root == num
