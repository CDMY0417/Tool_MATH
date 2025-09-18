def probability_no_event_all_days(probability_days: list[float]) -> float:
    probability_no_event = 1.0
    for probability in probability_days:
        probability_no_event *= probability
    return probability_no_event
