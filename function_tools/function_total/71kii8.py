def distance_from_origin_to_plane(a: float, b: float, c: float, d: float) -> float:
    import math
    numer = abs(d)
    denom = math.sqrt(a**2 + b**2 + c**2)
    return numer / denom
