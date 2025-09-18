def normalize_vector(vector: tuple, length: float):
    norm = (vector[0]**2 + vector[1]**2)**0.5
    return (length * vector[0] / norm, length * vector[1] / norm)
