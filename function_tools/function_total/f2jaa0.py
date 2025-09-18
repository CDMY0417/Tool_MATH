def vector_addition(v1: tuple[float, ...], v2: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(a + b for a, b in zip(v1, v2))
