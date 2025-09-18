def vector_norm_squared(p: list[float], q: list[float]) -> float:
    return sum((pi - qi) ** 2 for pi, qi in zip(p, q))
