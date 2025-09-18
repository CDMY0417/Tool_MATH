def compute_weekday_from_anchor(known_weekday: int, known_date: int, target_date: int) -> int:
    days_difference = known_date - target_date
    return (known_weekday - days_difference) % 7
