def point_plane_distance(a: int, b: int, c: int, d: int, x0: int, y0: int, z0: int) -> float:
    import math
    numerator = abs(a * x0 + b * y0 + c * z0 - d)
    denominator = math.sqrt(a ** 2 + b ** 2 + c ** 2)
    return numerator / denominator
