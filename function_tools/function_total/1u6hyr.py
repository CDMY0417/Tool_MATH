def vector_magnitude_squared(vector: tuple[float, ...]) -> float:
    return sum(component ** 2 for component in vector)
