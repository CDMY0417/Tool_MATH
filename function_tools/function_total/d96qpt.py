def probability_not_in_set(event_set: set, total_outcomes: int) -> float:
    return (total_outcomes - len(event_set)) / total_outcomes
