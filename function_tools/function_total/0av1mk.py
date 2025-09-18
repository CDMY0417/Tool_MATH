import math
def angle_subtraction_cosine(angle_a: float, angle_b: float) -> float:
    radians_a = math.radians(angle_a)
    radians_b = math.radians(angle_b)
    return math.cos(radians_a) * math.cos(radians_b) + math.sin(radians_a) * math.sin(radians_b)
