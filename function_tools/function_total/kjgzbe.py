def complete_the_square(a: float, b: float) -> tuple:
    h = b / (2 * a)
    k = -(b ** 2) / (4 * a)
    return h, k
