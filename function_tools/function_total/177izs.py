def is_unit_vector(vector: tuple[float, float, float]) -> bool:
    x, y, z = vector
    return abs(x**2 + y**2 + z**2 - 1) < 1e-9
