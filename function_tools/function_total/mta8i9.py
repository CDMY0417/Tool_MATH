def scale_triangle_sides(side_lengths: tuple[float, float, float], scale_factor: float) -> tuple[float, float, float]:
    return tuple(scale_factor * x for x in side_lengths)
