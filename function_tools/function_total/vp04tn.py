def dot_product(a: list[float], b: list[float]) -> float:
    return sum(ai * bi for ai, bi in zip(a, b))
