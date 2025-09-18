def add_vectors(vector1: list[float], vector2: list[float]) -> list[float]:
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]
