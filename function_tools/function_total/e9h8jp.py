def de_moivres_theorem_expansion(n: int, theta: float):
    from math import cos, sin
    real_part = cos(n * theta)
    imaginary_part = sin(n * theta)
    return real_part, imaginary_part
