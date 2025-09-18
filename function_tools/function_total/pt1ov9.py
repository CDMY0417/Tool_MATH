def dot_product(vector1: list[float], vector2: list[float]) -> float:
    return sum(x*y for x, y in zip(vector1, vector2))
