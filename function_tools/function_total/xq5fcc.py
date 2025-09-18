def apply_am_gm_inequality(terms: list[float]) -> float:
    product = 1
    n = len(terms)
    for term in terms:
        product *= term
    return n * (product ** (1/n))
