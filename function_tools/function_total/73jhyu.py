def dot_product(v1: tuple[float], v2: tuple[float]) -> float:
    return sum(x * y for x, y in zip(v1, v2))
