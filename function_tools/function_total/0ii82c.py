def sum_of_vectors(a: tuple, b: tuple) -> tuple:
    return tuple(a[i] + b[i] for i in range(len(a)))
