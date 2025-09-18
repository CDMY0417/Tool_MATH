def dot_product(vector1: tuple, vector2: tuple) -> float:
    return sum(a * b for a, b in zip(vector1, vector2))
