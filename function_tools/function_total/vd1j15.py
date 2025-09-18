def rotate_point(angle_degrees: float):
    from math import cos, sin, radians
    radians_angle = radians(angle_degrees)
    x = cos(radians_angle)
    y = sin(radians_angle)
    return (x, y)
