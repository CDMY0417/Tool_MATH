import math
def angle_between_vectors(dot_product: float, norm1: float, norm2: float) -> float:
    return math.degrees(math.acos(dot_product / (norm1 * norm2)))
