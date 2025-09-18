def weighted_sum(outcomes: list[float], frequencies: list[float]) -> float:
    return sum(o * f for o, f in zip(outcomes, frequencies))
