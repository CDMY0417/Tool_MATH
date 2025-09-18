def am_gm_inequality(values: list[float]) -> float:
    n = len(values)
    am = sum(values) / n
    gm_bound = am ** n
    return gm_bound
