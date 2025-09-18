def quadratic_has_no_real_roots(a: float, b: float, c: float) -> bool:
    discriminant = b**2 - 4*a*c
    return discriminant < 0
