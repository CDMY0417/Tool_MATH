def line_parameterization(point: tuple, direction_vector: tuple, t: float):
    return tuple(p + t * d for p, d in zip(point, direction_vector))
