def area_of_parallelogram(side1: float, side2: float, cos_angle: float) -> float:
    sin_angle = (1 - cos_angle ** 2) ** 0.5
    return side1 * side2 * sin_angle
