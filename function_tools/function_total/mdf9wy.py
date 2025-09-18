def sum_of_multiplied_terms(counts: list[float], terms: list[float]) -> float:
    return sum(c * t for c, t in zip(counts, terms))
