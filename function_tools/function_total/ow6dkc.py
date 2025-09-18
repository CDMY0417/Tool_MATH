def am_gm_inequality(terms: list[float]) -> bool:
    n = len(terms)
    product = 1
    for term in terms:
        product *= term
    return sum(terms) >= n * (product ** (1/n))
