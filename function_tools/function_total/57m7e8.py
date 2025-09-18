def expected_value(probabilities: list[float], outcomes: list[float]) -> float:
    return sum(p * x for p, x in zip(probabilities, outcomes))
