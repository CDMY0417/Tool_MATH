def trigonometric_sum_of_squares(x: float) -> float:
    from math import sin, cos
    return sin(x)**2 + (1/sin(x))**2 + cos(x)**2 + (1/cos(x))**2
