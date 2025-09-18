def weighted_vector_sum(x: float, v1: tuple[float, float], y: float, v2: tuple[float, float], z: float, v3: tuple[float, float]) -> tuple[float, float]:
    return (x * v1[0] + y * v2[0] + z * v3[0], x * v1[1] + y * v2[1] + z * v3[1])
