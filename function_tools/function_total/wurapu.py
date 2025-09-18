def vector_from_point_to_line(point: tuple, line_point: tuple):
    return tuple(lp - p for lp, p in zip(line_point, point))
