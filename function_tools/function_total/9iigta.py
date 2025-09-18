def vector_magnitude_squared(v: tuple) -> float:
    return sum(v[i] ** 2 for i in range(len(v)))
