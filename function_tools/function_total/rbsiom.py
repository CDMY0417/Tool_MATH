def cos_angle_subtraction(a: float, b: float) -> float:
    from math import cos, sin, radians
    return cos(radians(a)) * cos(radians(b)) + sin(radians(a)) * sin(radians(b))
