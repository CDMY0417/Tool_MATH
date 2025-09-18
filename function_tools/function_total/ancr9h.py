def probability_no_replacement(counts: list[int], total: int, k: int) -> float:
    assert len(counts) >= k, 'Not enough items to select.'
    probability = 1.0
    for i in range(k):
        probability *= counts[i] / total
        total -= 1
        counts[i] -= 1
    return probability
