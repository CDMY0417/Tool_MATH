def vector_subtraction(v1: tuple[float, float, float], v2: tuple[float, float, float]) -> tuple[float, float, float]:
    return tuple(v1[i] - v2[i] for i in range(3))
