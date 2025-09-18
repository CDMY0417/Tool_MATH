def probability_of_successive_events(probabilities: list[float]) -> float:
    result = 1.0
    for probability in probabilities:
        result *= probability
    return result
