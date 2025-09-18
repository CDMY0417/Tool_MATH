def project_onto_vector(vector: tuple[float, float]):
    a1, a2 = vector
    scale = 1 / (a1 ** 2 + a2 ** 2)
    return ((scale * a1 ** 2, scale * a1 * a2), (scale * a1 * a2, scale * a2 ** 2))
