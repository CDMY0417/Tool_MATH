def cotangent_difference(x: float) -> float:
    from math import cos, sin
    return (cos(x) / sin(x)) - (cos(2 * x) / sin(2 * x))
