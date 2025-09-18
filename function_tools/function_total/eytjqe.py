def rotate_point_on_unit_circle(point: tuple[float, float], theta_degrees: float) -> tuple[float, float]:
    import math
    theta_radians = math.radians(theta_degrees)
    x, y = point
    new_x = x * math.cos(theta_radians) - y * math.sin(theta_radians)
    new_y = x * math.sin(theta_radians) + y * math.cos(theta_radians)
    return (new_x, new_y)
