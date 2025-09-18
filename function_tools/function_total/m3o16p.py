def point_on_line(base_point: tuple, direction_vector: tuple, t: float) -> tuple:
    return tuple(bp + t * dv for bp, dv in zip(base_point, direction_vector))
