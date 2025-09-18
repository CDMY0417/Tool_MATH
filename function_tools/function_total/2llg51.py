def vector_addition(vec1: tuple, vec2: tuple):
    return tuple(a + b for a, b in zip(vec1, vec2))
