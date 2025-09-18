def dot_product(vec1: tuple, vec2: tuple) -> float:
    return sum(x * y for x, y in zip(vec1, vec2))
