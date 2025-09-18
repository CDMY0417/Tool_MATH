import math
def tangent(angle_degrees: float) -> float:
    radians = math.radians(angle_degrees)
    return math.sin(radians) / math.cos(radians)
