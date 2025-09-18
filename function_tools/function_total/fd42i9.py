def nonzero_scalar_multiple(vector1: tuple, vector2: tuple) -> bool:
    x1, y1 = vector1
    x2, y2 = vector2
    if (x1, y1) == (0, 0) or (x2, y2) == (0, 0):
        return False
    if x1 == 0 or x2 == 0:
        return y1 / x1 == y2 / x2
    return y1 / x1 == y2 / x2
