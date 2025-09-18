def multiply_vector_by_scalar(vector: tuple[float, float, float], scalar: float) -> tuple[float, float, float]:
    return tuple(scalar * component for component in vector)
