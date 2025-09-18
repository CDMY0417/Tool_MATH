def roots_of_unity_angles(angle: float, n: int):
    return [(angle + 360 * k) / n for k in range(n)]
