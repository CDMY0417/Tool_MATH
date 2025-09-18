def find_point_on_line(start_point: tuple, direction_vector: tuple, scalar: float):
    return tuple(p + scalar * d for p, d in zip(start_point, direction_vector))
