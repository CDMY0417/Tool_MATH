def dot_product(vec1: list[float], vec2: list[float]) -> float:
    return sum(x * y for x, y in zip(vec1, vec2))
