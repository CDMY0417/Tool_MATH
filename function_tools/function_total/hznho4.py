def is_direction_vector(vector: tuple, slope: float) -> bool:
    x, y = vector
    return x != 0 and y / x == slope
