def scalar_multiply_vector(scalar: float, vector: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(scalar * x for x in vector)
