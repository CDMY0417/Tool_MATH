def complete_square(a: int, b: int, c: int) -> tuple[int, float, float]:
    h = -b / (2 * a)
    k = c - a * h ** 2
    return a, h, k
