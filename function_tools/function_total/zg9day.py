def calculate_probability(successful: int, total: int) -> float:
    if total == 0:
        return 0.0
    return successful / total
