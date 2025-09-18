def calculate_remaining_sum(mean: float, total_tests: int, known_scores: list[float]) -> float:
    return mean * total_tests - sum(known_scores)
