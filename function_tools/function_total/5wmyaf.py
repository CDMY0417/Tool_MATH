def complete_square(a: float, b: float) -> tuple:
    h = -b / (2 * a)
    constant = a * h**2 - b * h
    return h, constant
