def is_perfect_square(number: int) -> bool:
    if number < 0:
        return False
    root = int(number**0.5)
    return root * root == number
