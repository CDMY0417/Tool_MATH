def triangle_centroid(P: tuple[float, float], Q: tuple[float, float], R: tuple[float, float]) -> tuple[float, float]:
    return ((P[0] + Q[0] + R[0]) / 3, (P[1] + Q[1] + R[1]) / 3)
