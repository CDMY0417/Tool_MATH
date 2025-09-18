def cesaro_sum_with_prefix(prefix: int, sequence: list[int]) -> float:
    n = len(sequence) + 1
    total_sum = prefix
    cumulative_sum = prefix
    for num in sequence:
        cumulative_sum += num
        total_sum += cumulative_sum
    return total_sum / n
