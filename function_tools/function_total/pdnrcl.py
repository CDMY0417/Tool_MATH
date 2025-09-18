def centroid_of_triangle(vertex_a: tuple[float, float], vertex_b: tuple[float, float], vertex_c: tuple[float, float]) -> tuple[float, float]:
    x_centroid = (vertex_a[0] + vertex_b[0] + vertex_c[0]) / 3
    y_centroid = (vertex_a[1] + vertex_b[1] + vertex_c[1]) / 3
    return (x_centroid, y_centroid)
