import math

def projected_length(length: float, angle_deg: float) -> float:
    return length * math.sin(math.radians(angle_deg))
