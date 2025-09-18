def num_real_solutions_quadratic(a: float, b: float, c: float) -> int:
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        return 2
    elif discriminant == 0:
        return 1
    else:
        return 0
