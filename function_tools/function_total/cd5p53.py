def euclidean_distance(v1: tuple[float, ...], v2: tuple[float, ...]) -> float:
    return sum((i - j) ** 2 for i, j in zip(v1, v2)) ** 0.5
