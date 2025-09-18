def projection_of_vector(u: tuple[float, float], v: tuple[float, float]) -> tuple[float, float]:
    dot_product_uv = u[0] * v[0] + u[1] * v[1]
    dot_product_vv = v[0] * v[0] + v[1] * v[1]
    scalar = dot_product_uv / dot_product_vv
    return (scalar * v[0], scalar * v[1])
