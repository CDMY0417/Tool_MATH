def years_until_age_ratio(current_age1: int, current_age2: int, target_ratio: int) -> int:
    x = (target_ratio * current_age2 - current_age1) // (1 - target_ratio)
    return x
