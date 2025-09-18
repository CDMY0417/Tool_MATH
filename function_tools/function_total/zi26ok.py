def magnitude_squared(vec1: tuple, vec2: tuple) -> float:
    return sum((v1 - v2) ** 2 for v1, v2 in zip(vec1, vec2))
