def dot_product(vector1: list[float], vector2: list[float]) -> float:
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
