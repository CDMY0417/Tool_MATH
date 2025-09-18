def probability_of_event(successful_outcomes: int, total_outcomes: int) -> float:
    if total_outcomes == 0:
        return 0.0
    return successful_outcomes / total_outcomes
