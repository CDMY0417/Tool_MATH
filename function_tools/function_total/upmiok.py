def cosine_of_angle_difference(angle1: float, angle2: float) -> float:
    from math import cos, radians, sin
    return cos(radians(angle1)) * cos(radians(angle2)) + sin(radians(angle1)) * sin(radians(angle2))
