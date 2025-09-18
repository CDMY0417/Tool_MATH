def probability_product(probabilities: list[float]) -> float:
    product = 1.0
    for p in probabilities:
        product *= p
    return product
