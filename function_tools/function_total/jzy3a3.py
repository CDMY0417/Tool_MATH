def rotate_point(angle_degrees: float):
    import math
    angle_radians = math.radians(angle_degrees)
    return (math.cos(angle_radians), math.sin(angle_radians))
