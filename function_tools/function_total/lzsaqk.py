def midpoint(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> tuple[float, float, float]:
    return tuple((p1 + p2) / 2 for p1, p2 in zip(point1, point2))
