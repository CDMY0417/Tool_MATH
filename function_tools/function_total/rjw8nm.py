def dot_product(vector1: tuple[float, ...], vector2: tuple[float, ...]) -> float:
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
