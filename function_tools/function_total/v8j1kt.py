def complete_square(a: int, b: int) -> tuple:
    h = -b / (2 * a)
    c = - (b**2) / (4 * a)
    return h, c
