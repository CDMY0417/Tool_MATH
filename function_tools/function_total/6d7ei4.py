def is_perfect_cube(number: int) -> bool:
    cube_root = round(number ** (1/3))
    return cube_root ** 3 == number
