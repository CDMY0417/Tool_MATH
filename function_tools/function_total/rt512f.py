def vector_subtraction(a: tuple, b: tuple):
    return tuple(ai - bi for ai, bi in zip(a, b))
