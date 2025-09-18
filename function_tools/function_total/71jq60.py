def compute_other_leg(hypotenuse: float, known_leg: float) -> float:
    import math
    return math.sqrt(hypotenuse**2 - known_leg**2)
