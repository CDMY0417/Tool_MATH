def law_of_cosines(b: float, c: float, cos_angle: float) -> float:
    a_squared = b**2 + c**2 - 2 * b * c * cos_angle
    return a_squared**0.5
