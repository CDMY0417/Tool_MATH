def vector_magnitude(vector: tuple) -> float:
    import math
    return math.sqrt(sum(component**2 for component in vector))
