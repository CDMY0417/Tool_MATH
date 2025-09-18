def dot_product(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    return sum(ai * bi for ai, bi in zip(a, b))
