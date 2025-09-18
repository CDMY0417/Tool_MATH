def semi_major_axis_length(point1: tuple, point2: tuple) -> float:
    length = abs(point1[0] - point2[0]) / 2
    return length
