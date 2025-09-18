def subtract_vectors(a: list[float], b: list[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]
