def magnitude_product(v1: tuple[float, ...], v2: tuple[float, ...]) -> float:
    import math
    return math.sqrt(sum(x**2 for x in v1)) * math.sqrt(sum(y**2 for y in v2))
