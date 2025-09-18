def am_gm_inequality(values: list[float]) -> bool:
    import math
    n = len(values)
    return sum(values) / n >= math.prod(values) ** (1/n)
