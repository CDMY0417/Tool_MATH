def cross_product(vectors_a: list[float], vectors_b: list[float]) -> list[float]:
    return [vectors_a[1] * vectors_b[2] - vectors_a[2] * vectors_b[1], vectors_a[2] * vectors_b[0] - vectors_a[0] * vectors_b[2], vectors_a[0] * vectors_b[1] - vectors_a[1] * vectors_b[0]]
