def mean_from_histogram(frequencies: list[int]) -> float:
    total_sum = sum(i * freq for i, freq in enumerate(frequencies))
    total_count = sum(frequencies)
    return total_sum / total_count
