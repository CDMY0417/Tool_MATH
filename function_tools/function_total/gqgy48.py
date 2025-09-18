def am_gm_inequality(values: list[float]) -> float:
    n = len(values)
    product = 1
    for v in values:
        product *= v
    return n * (product ** (1/n))
