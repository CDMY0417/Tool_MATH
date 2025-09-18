def complete_square(a: float, b: float):
    h = -b / (2 * a)
    return h, a * h**2 + b * h
