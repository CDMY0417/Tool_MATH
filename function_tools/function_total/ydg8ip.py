def vector_subtraction(a: tuple, b: tuple) -> tuple:
    return tuple(a_i - b_i for a_i, b_i in zip(a, b))
