import math

def rotate_point(point: tuple[float, float], angle_degrees: float):
    angle_radians = math.radians(angle_degrees)
    cos_angle = math.cos(angle_radians)
    sin_angle = math.sin(angle_radians)
    x, y = point
    x_new = cos_angle * x - sin_angle * y
    y_new = sin_angle * x + cos_angle * y
    return (x_new, y_new)
