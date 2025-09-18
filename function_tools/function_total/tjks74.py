def calculate_plane_distance(a: int, b: int, c: int, d: int, x: int, y: int, z: int) -> float:
    return abs(a * x + b * y + c * z + d) / (a**2 + b**2 + c**2)**0.5
