def is_perpendicular(vector1: tuple[float, float], vector2: tuple[float, float]) -> bool:
    return vector1[0] * vector2[0] + vector1[1] * vector2[1] == 0
