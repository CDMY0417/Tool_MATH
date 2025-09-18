def is_cube_of_integer(number: int) -> bool:
    root = round(number ** (1/3))
    return root ** 3 == number
