def centroid_coordinates(vertex1: tuple[float, float], vertex2: tuple[float, float], vertex3: tuple[float, float]) -> tuple[float, float]:
    x_c = (vertex1[0] + vertex2[0] + vertex3[0]) / 3
    y_c = (vertex1[1] + vertex2[1] + vertex3[1]) / 3
    return (x_c, y_c)
