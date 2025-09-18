def distance_along_normal(point: tuple, normal_vector: tuple, plane_constant: int):
    x, y, z = point
    a1, a2, a3 = normal_vector
    t = (plane_constant - (a1 * x + a2 * y + a3 * z)) / (a1**2 + a2**2 + a3**2)
    return t
