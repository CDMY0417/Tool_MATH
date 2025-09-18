def vector_between_points(point1: tuple[float, ...], point2: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(p2 - p1 for p1, p2 in zip(point1, point2))
