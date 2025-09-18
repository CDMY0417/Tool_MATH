def is_perfect_square(x: int) -> bool:
    root = int(x ** 0.5)
    return root * root == x
