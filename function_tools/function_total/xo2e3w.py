def complete_the_square(a: int, b: int, c: int) -> tuple:
    h = -b / (2 * a)
    k = c - (b**2) / (4 * a)
    return (h, k)
