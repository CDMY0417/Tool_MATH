def midpoint_vector(A: tuple[float, ...], B: tuple[float, ...]) -> tuple[float, ...]:
    return tuple((a + b) / 2 for a, b in zip(A, B))
