def scalar_multiplication(scalar: float, vector: tuple[float, ...]) -> tuple[float, ...]:
    return tuple(scalar * v for v in vector)
