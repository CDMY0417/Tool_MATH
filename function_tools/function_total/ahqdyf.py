def projection_onto_vector(v: tuple[float, float], u: tuple[float, float]) -> tuple[float, float]:
    dot_product = v[0] * u[0] + v[1] * u[1]
    norm_squared = u[0] * u[0] + u[1] * u[1]
    scalar = dot_product / norm_squared
    return (scalar * u[0], scalar * u[1])
