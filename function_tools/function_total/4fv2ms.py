def reflect_through_xy_plane(vector: tuple[float, float, float]) -> tuple[float, float, float]:
    x, y, z = vector
    return (x, y, -z)
