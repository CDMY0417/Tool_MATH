def cos_within_pi_interval(angle: float):
    import math
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle < 0:
        angle += 2 * math.pi
    return angle
