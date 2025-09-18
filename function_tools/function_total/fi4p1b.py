def centroid_vector(A: tuple, B: tuple, C: tuple):
    return tuple((a + b + c) / 3 for a, b, c in zip(A, B, C))
