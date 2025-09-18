def midpoint_of_vectors(a: tuple[float, ...], b: tuple[float, ...]) -> tuple[float, ...]:
    return tuple((a[i] + b[i]) / 2 for i in range(len(a)))
