def cotangent(degrees: float) -> float:
    import math
    radians = math.radians(degrees)
    cosine = math.cos(radians)
    sine = math.sin(radians)
    return cosine / sine if sine != 0 else float('inf')
