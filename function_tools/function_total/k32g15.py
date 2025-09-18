def vector_magnitude_squared(u: tuple[float, ...], v: tuple[float, ...]) -> float:
    return sum((x + y) ** 2 for x, y in zip(u, v))
