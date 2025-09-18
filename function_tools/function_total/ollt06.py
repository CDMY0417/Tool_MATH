def scale_equation(eq: tuple, factor: float):
    scaled_eq = tuple(a * factor for a in eq)
    return scaled_eq
