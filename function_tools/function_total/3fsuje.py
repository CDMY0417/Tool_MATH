def line_equation_from_points(x1: float, y1: float, x2: float, y2: float) -> tuple:
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    return (A, B, C)
