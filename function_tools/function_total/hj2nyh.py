def vector_subtraction(a: tuple, b: tuple):
    return tuple(a[i] - b[i] for i in range(len(a)))
