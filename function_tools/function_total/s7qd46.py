def complete_the_square(a: float, b: float, c: float):
    h = b / (2 * a)
    k = c - a * h**2
    return h, k
