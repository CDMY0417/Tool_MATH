def length_by_coordinates(pt1: tuple[float, float], pt2: tuple[float, float]) -> float:
    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5
