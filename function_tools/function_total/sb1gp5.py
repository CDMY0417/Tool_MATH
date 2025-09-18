def cosine_subtraction_formula(angle1: float, angle2: float) -> float:
    import math
    return math.cos(math.radians(angle1)) * math.cos(math.radians(angle2)) + math.sin(math.radians(angle1)) * math.sin(math.radians(angle2))
