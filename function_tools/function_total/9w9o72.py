def probability_of_one_absent(p1: float, p2: float) -> float:
    return p1 * (1 - p2) + (1 - p1) * p2
