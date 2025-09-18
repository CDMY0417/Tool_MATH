def cesaro_sum(sequence: list[float]) -> float:
    n = len(sequence)
    total_sum = 0
    cumulative_sum = 0
    for num in sequence:
        cumulative_sum += num
        total_sum += cumulative_sum
    return total_sum / n
