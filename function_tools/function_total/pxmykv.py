def parametric_line_point(start: tuple[float, float, float], end: tuple[float, float, float], t: float) -> tuple[float, float, float]:
    return ((1-t) * start[0] + t * end[0], (1-t) * start[1] + t * end[1], (1-t) * start[2] + t * end[2])
