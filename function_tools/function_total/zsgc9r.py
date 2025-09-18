def distance_between_collinear_points(point1: tuple[int, int], point2: tuple[int, int]) -> float:
    if point1[0] == point2[0]:
        return abs(point2[1] - point1[1])
    return abs(point2[0] - point1[0])
