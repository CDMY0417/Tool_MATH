def law_of_cosines_to_find_angle(a: float, b: float, c: float) -> float:
    import math
    cos_angle = (a**2 + b**2 - c**2) / (2 * a * b)
    return cos_angle
