def law_of_cosines_length(a: float, b: float, angle_c: float) -> float:
    from math import cos
    return (a**2 + b**2 - 2*a*b*cos(angle_c))**0.5
