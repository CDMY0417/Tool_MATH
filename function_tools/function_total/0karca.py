def probability_of_outcome(total_trials: int, prob_event: float, times_event_occurs: int):
    return (prob_event ** times_event_occurs) * ((1 - prob_event) ** (total_trials - times_event_occurs))
