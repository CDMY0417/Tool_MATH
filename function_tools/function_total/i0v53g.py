import math

def law_of_cosines(side1: float, side2: float, angle_deg: float) -> float:
    angle_rad = math.radians(angle_deg)
    return math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(angle_rad))
