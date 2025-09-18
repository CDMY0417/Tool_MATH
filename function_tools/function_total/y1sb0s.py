def vector_addition(vector1: tuple, vector2: tuple) -> tuple:
    return tuple(v1 + v2 for v1, v2 in zip(vector1, vector2))
