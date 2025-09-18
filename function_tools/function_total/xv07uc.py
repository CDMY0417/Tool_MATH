def distance_between_points(p1: tuple, p2: tuple) -> int:
    return abs(p1[0] - p2[0]) if p1[1] == p2[1] else abs(p1[1] - p2[1])
