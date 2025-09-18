def complete_square(a: int, b: int):
    h = b / (2 * a)
    k = -h * h * a
    return (h, k)
