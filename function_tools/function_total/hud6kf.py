def double_angle_formula(A: float) -> float:
    from math import sin, cos, radians
    angle = radians(A)
    return -2 * sin(angle) * cos(angle)
