def vector_projection(v: tuple, u: tuple) -> tuple:
    dot_product = v[0] * u[0] + v[1] * u[1]
    magnitude_u_squared = u[0] ** 2 + u[1] ** 2
    scale_factor = dot_product / magnitude_u_squared
    return (scale_factor * u[0], scale_factor * u[1])
