def magnitude(vector: tuple[float, ...]) -> float:
    return sum(v**2 for v in vector) ** 0.5
