def vector_subtraction(a: tuple, b: tuple) -> tuple:
    return tuple(x - y for x, y in zip(a, b))
