def scale_and_subtract_equations(eq1: tuple, eq2: tuple, scale1: int, scale2: int) -> tuple:
    scaled_eq1 = tuple(scale1 * term for term in eq1)
    scaled_eq2 = tuple(scale2 * term for term in eq2)
    return tuple(s1 - s2 for s1, s2 in zip(scaled_eq1, scaled_eq2))
