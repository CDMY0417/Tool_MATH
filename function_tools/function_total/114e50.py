def next_perfect_square(number: int) -> int:
    root = int(number**0.5)
    if root * root == number:
        root += 1
    return (root + 1) * (root + 1)
