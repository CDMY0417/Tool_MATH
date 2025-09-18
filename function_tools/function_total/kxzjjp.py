def dot_product(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    return sum(a_i * b_i for a_i, b_i in zip(a, b))
