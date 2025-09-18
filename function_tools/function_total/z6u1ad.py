def calculate_percentage_increase(initial_value: float, percentage: float) -> float:
    increase = initial_value * (percentage / 100)
    return initial_value + increase
