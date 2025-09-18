def dot_product(vector_a: list[float], vector_b: list[float]) -> float:
    return sum(x * y for x, y in zip(vector_a, vector_b))
