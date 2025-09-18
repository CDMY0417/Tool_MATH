def distance_formula(point1: tuple[float, ...], point2: tuple[float, ...]) -> float:
    return sum((c1 - c2) ** 2 for c1, c2 in zip(point1, point2)) ** 0.5
