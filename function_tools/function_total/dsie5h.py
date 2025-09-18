def calculate_probability(successful: int, total: int) -> float:
    return successful / total if total > 0 else 0
