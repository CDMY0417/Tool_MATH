def reflection_matrix(angle_degrees: float):
    import math
    theta_radians = math.radians(angle_degrees)
    return [[math.cos(2 * theta_radians), math.sin(2 * theta_radians)],
            [math.sin(2 * theta_radians), -math.cos(2 * theta_radians)]]
