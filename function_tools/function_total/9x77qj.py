def is_perfect_cube(num: int) -> bool:
    root = round(num ** (1/3))
    return root ** 3 == num
