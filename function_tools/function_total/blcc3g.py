def calculate_probability(favorable: int, total: int) -> float:
    if total == 0:
        return 0.0
    return favorable / total
