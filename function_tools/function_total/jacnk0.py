def dot_product(vector1: tuple[float], vector2: tuple[float]) -> float:
    return sum(component1 * component2 for component1, component2 in zip(vector1, vector2))
