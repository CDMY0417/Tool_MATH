def distance_point_to_plane(point: tuple[float, float, float], plane_coeffs: tuple[float, float, float, float]) -> float:
    a, b, c, d = plane_coeffs
    x, y, z = point
    return abs(a*x + b*y + c*z + d) / (a**2 + b**2 + c**2) ** 0.5
