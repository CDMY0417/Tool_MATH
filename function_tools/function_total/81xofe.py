def cross_product(u: tuple[float, float, float], v: tuple[float, float, float]) -> tuple[float, float, float]:
    cx = u[1] * v[2] - u[2] * v[1]
    cy = u[2] * v[0] - u[0] * v[2]
    cz = u[0] * v[1] - u[1] * v[0]
    return (cx, cy, cz)
