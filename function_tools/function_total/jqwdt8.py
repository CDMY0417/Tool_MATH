def apply_am_gm_inequality(terms: list[float]) -> bool:
    product = 1
    for term in terms:
        product *= term
    k = len(terms)
    return sum(terms) >= k * (product ** (1/k))
