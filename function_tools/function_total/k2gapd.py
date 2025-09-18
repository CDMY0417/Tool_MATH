def probability_greater_sum(sums: dict, max_number: int) -> float:
    p_each = 1 / max_number
    total_prob = 0
    for number in range(max_number, 0, -1):
        success_prob = 0
        for s in sums:
            if number > s:
                success_prob += sums[s] / 10
        total_prob += success_prob * p_each
    return total_prob
