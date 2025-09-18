def de_moivre_theorem(theta: float, n: int):
    import math
    cos_n_theta = math.cos(math.radians(n * theta))
    sin_n_theta = math.sin(math.radians(n * theta))
    return cos_n_theta, sin_n_theta
