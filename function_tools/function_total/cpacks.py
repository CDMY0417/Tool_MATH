def apply_cauchy_schwarz(seq1: list[float], seq2: list[float]) -> float:
    assert len(seq1) == len(seq2)
    sum1 = sum(seq1[i] * seq2[i] for i in range(len(seq1)))
    sum2 = sum(val ** 2 for val in seq1)
    sum3 = sum(val ** 2 for val in seq2)
    return sum1**2 / (sum2 * sum3)
