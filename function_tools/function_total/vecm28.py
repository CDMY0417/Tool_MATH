def distance_between_points(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> float:
    return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5
