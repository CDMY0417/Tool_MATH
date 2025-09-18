def apply_cauchy_schwarz(sequence1: list[float], sequence2: list[float]) -> bool:
    sum1 = sum(sequence1)
    sum2_reciprocal = sum([1/x for x in sequence2])
    return (sum1 * sum2_reciprocal) >= (len(sequence1))**2
