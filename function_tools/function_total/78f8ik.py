import math

def law_of_cosines_third_side(side1: float, side2: float, angle_degree: float) -> float:
    angle_radian = math.radians(angle_degree)
    return (side1**2 + side2**2 - 2 * side1 * side2 * math.cos(angle_radian))**0.5
