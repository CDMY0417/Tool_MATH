def minimize_quadratic(a: int, b: int, c: int) -> int:
    vertex = -b / (2 * a)
    return round(vertex)
