def vector_addition(vector1: list[float], vector2: list[float]) -> list[float]:
    return [a + b for a, b in zip(vector1, vector2)]
