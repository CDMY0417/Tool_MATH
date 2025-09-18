def expected_value(outcomes: list[float], probabilities: list[float]) -> float:
    return sum(o * p for o, p in zip(outcomes, probabilities))
