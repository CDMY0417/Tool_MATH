def law_of_cosines(a: float, b: float, angle_c_cos: float) -> float:
    return (a**2 + b**2 - 2*a*b*angle_c_cos)**0.5
