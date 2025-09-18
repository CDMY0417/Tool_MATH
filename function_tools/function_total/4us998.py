def product_to_sum_formula(angle1_degrees: float, angle2_degrees: float) -> float:
    import math
    return (math.sin(math.radians(angle1_degrees + angle2_degrees)) + math.sin(math.radians(angle1_degrees - angle2_degrees))) / 2
