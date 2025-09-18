def probability_of_independent_events(probabilities: list[float]) -> float:
    result = 1.0
    for p in probabilities:
        result *= p
    return result
