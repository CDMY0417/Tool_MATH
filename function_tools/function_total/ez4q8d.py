def weighted_sum(averages: list[float], counts: list[int]) -> float:
    return sum(avg * count for avg, count in zip(averages, counts))
