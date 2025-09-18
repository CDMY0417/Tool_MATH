def vector_addition(vector1: list[float], vector2: list[float]) -> list[float]:
    return [x + y for x, y in zip(vector1, vector2)]
