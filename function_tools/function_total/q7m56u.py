def vector_triple_product(a: tuple[float, float, float], b: tuple[float, float, float], c: tuple[float, float, float]) -> tuple[float, float, float]:
    a_dot_c = sum(a[i] * c[i] for i in range(3))
    a_dot_b = sum(a[i] * b[i] for i in range(3))
    return tuple((a_dot_c * b[i] - a_dot_b * c[i]) for i in range(3))
