def calculate_centroid(vertex1: tuple[float, float], vertex2: tuple[float, float], vertex3: tuple[float, float]) -> tuple[float, float]:
    return ((vertex1[0] + vertex2[0] + vertex3[0]) / 3, (vertex1[1] + vertex2[1] + vertex3[1]) / 3)
