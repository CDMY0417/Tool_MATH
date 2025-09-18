def dot_product(v1: dict, v2: dict) -> float:
    return sum(v1[key] * v2[key] for key in v1)
