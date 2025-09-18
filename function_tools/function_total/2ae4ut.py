def plane_equation_substitute(normal: tuple, point: tuple) -> float:
    return -(normal[0] * point[0] + normal[1] * point[1] + normal[2] * point[2])
