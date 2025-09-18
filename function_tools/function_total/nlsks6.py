def project_vector(v: tuple, u: tuple) -> tuple:
    dot_product = v[0] * u[0] + v[1] * u[1]
    magnitude_squared = u[0]**2 + u[1]**2
    scalar = dot_product / magnitude_squared
    return tuple(scalar * u[i] for i in range(len(u)))
