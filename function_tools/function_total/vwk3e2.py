def vector_difference(vector_a: tuple[float, float, float], vector_b: tuple[float, float, float]) -> tuple[float, float, float]:
    return tuple(a - b for a, b in zip(vector_a, vector_b))
