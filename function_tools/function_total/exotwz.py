def vector_norm(v: list[float]) -> float:
    return sum(x*x for x in v) ** 0.5
