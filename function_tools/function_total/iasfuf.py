def probability_of_event(event_probs: list[float]) -> float:
    from functools import reduce
    from operator import mul
    return reduce(mul, event_probs)
