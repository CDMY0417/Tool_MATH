def complete_the_square(a: float, b: float, c: float):
    h = b / (2 * a)
    k = c - (b**2 / (4 * a))
    return (a, h, k)
