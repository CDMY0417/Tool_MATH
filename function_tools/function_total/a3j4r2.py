def euclidean_distance(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    import math
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
