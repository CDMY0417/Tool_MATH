def is_point_on_line(point: tuple, m: float, c: float) -> bool:
    x, y = point
    return y == (m * x) + c
