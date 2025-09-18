def calculate_centroid_of_triangle(v1: tuple[float, float, float], v2: tuple[float, float, float], v3: tuple[float, float, float]) -> tuple[float, float, float]:
    x = (v1[0] + v2[0] + v3[0]) / 3
    y = (v1[1] + v2[1] + v3[1]) / 3
    z = (v1[2] + v2[2] + v3[2]) / 3
    return (x, y, z)
