def geometric_series_sum_exceeds_target(initial_term: int, ratio: int, target: int) -> int:
    n = 0
    current_sum = 0
    while current_sum <= target:
        current_sum += initial_term * (ratio ** n)
        n += 1
    return n - 1
