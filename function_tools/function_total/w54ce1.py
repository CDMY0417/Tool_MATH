def percent_increase(original_value: float, new_value: float) -> float:
    increase = new_value - original_value
    percent = (increase / original_value) * 100
    return percent
