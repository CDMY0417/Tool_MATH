def sin_half_angle(sin_theta: float) -> float:
    from math import sqrt
    return sqrt((1 - sqrt(1 - sin_theta**2)) / 2)
