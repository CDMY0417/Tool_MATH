def weighted_sum(values: list, weights: list) -> int:
    return sum(value * weight for value, weight in zip(values, weights))
