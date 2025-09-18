def is_perpendicular(vector1: tuple, vector2: tuple) -> bool:
    return vector1[0]*vector2[0] + vector1[1]*vector2[1] == 0
