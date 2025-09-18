def vector_from_points(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> tuple[float, float, float]:
    return (point2[0] - point1[0], point2[1] - point1[1], point2[2] - point1[2])
