def cosecant_of_angle(angle: float) -> float:
    import math
    return 1 / math.sin(math.radians(angle)) if angle != 0 else float('inf')
