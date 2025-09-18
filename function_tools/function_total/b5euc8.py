def complete_the_square(a: int, b: int) -> tuple[float, float]:
    h = b / (2 * a)
    k = (b ** 2) / (4 * a)
    return h, k
