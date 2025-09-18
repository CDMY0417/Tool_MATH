def rotation_matrix(theta: float):
    import math
    return [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
