def probability_of_event(p: float, k: int, total_trials: int) -> float:
    return (p ** k) * ((1 - p) ** (total_trials - k))
