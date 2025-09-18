def distance_squared(point1: tuple[float, ...], point2: tuple[float, ...]) -> float:
    return sum((x1 - x2) ** 2 for x1, x2 in zip(point1, point2))
