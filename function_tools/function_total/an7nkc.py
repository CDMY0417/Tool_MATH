def find_hyperbola_center(vertex1: tuple[float, float], vertex2: tuple[float, float]) -> tuple[float, float]:
    x_center = (vertex1[0] + vertex2[0]) / 2
    y_center = (vertex1[1] + vertex2[1]) / 2
    return (x_center, y_center)
