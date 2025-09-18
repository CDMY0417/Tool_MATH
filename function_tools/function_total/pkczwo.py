def midpoint(point1: tuple[float, ...], point2: tuple[float, ...]) -> tuple[float, ...]:
    return tuple((x1 + x2) / 2 for x1, x2 in zip(point1, point2))
