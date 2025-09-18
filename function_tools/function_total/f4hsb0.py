def absolute_ratio_of_sums_and_differences(a: float, b: float) -> float:
    numerator = (a + b) ** 2
    denominator = (a - b) ** 2
    return abs((numerator / denominator) ** 0.5)
