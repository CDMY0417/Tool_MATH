def complete_square(a: int, b: int):
    h = b / (2 * a)
    k = a * h ** 2
    return h, k
