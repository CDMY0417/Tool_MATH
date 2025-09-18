def solve_hyperbola_foci_distance(a_squared: float, b_squared: float) -> float:
    import math
    c_squared = a_squared + b_squared
    c = math.sqrt(c_squared)
    return 2 * c
