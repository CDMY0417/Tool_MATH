def is_perfect_cube(number: int) -> bool:
    root = round(number ** (1/3))
    return root ** 3 == number
