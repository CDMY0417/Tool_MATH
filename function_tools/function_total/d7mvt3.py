def am_gm_inequality(terms: list[float]) -> float:
    n = len(terms)
    product = 1
    for term in terms:
        product *= term
    return n * (product ** (1/n))
