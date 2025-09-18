def law_of_cosines(a: float, b: float, cos_angle: float) -> float:
    from math import sqrt
    return sqrt(a**2 + b**2 - 2 * a * b * cos_angle)
