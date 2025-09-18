def dot_product(vector_a: list[float], vector_b: list[float]) -> float:
    return sum(a * b for a, b in zip(vector_a, vector_b))
