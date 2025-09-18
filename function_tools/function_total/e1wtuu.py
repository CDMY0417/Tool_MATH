def reflect_vector(v: tuple, d: tuple):
    scalar_projection = (v[0] * d[0] + v[1] * d[1]) / (d[0] ** 2 + d[1] ** 2)
    reflection = (2 * scalar_projection * d[0] - v[0], 2 * scalar_projection * d[1] - v[1])
    return reflection
