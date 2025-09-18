def weighted_sum(values: list[int], counts: list[int]) -> int:
    return sum(value * count for value, count in zip(values, counts))
