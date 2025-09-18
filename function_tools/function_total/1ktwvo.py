def tan_of_angle(numerator: float, denominator: float) -> float:
    import math
    return math.tan(math.atan2(numerator, denominator))
