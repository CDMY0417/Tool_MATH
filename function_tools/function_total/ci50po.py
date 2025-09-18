def equality_conditions(ratios: tuple, total_sum: float):
    k = total_sum / sum(ratios)
    return tuple(k * ratio for ratio in ratios)
