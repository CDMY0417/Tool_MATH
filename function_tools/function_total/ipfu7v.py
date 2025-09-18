def cross_product(vector_a: tuple[float, float, float], vector_b: tuple[float, float, float]) -> tuple[float, float, float]:
    cp_x = vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1]
    cp_y = vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2]
    cp_z = vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
    return (cp_x, cp_y, cp_z)
