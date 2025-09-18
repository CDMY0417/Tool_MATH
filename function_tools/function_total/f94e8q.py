def find_plane_equation_constant(point: tuple[float, float, float], normal: tuple[float, float, float]) -> float:
    return sum(p * n for p, n in zip(point, normal))
