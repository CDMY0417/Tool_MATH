def product_to_sum(angle1: float, angle2: float) -> float:
    from math import cos
    return cos(angle1 + angle2) + cos(angle1 - angle2)
