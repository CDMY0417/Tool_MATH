def polar_to_rectangular(r: float, theta_degrees: float):
    import math
    theta_radians = math.radians(theta_degrees)
    return r * math.cos(theta_radians), r * math.sin(theta_radians)
