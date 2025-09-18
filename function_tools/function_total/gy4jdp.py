def weighted_average(weights: list[float], expected_values: list[float]) -> float:
    return sum(w * e for w, e in zip(weights, expected_values))
