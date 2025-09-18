def complete_the_square(a: float, b: float) -> tuple[float, float]:
    h = -b / (2 * a)
    k = a * h**2 + b * h
    return h, k
