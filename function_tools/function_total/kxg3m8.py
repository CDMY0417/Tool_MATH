def complete_square(a: float, b: float):
    h = b / (2 * a)
    k = a * h**2
    return h, k
