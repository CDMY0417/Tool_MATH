def scalar_multiplication(scalar: int, vector: tuple) -> tuple:
    return tuple(scalar * vector[i] for i in range(3))
