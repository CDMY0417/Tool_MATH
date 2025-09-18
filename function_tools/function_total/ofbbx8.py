def cross_product(vector_a: list[float], vector_b: list[float]) -> list[float]:
    return [vector_a[1]*vector_b[2] - vector_a[2]*vector_b[1], vector_a[2]*vector_b[0] - vector_a[0]*vector_b[2], vector_a[0]*vector_b[1] - vector_a[1]*vector_b[0]]
