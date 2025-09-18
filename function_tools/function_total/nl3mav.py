def probability_product(probabilities: list[float]) -> float:
    result = 1.0
    for p in probabilities:
        result *= p
    return result
