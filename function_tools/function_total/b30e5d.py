def polar_to_rectangular(r: float, theta: float):
    from math import cos, sin
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
