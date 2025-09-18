def vector_magnitude_squared(vector: dict) -> float:
    return sum(coordinate ** 2 for coordinate in vector.values())
