def log_change_of_base(log_value: float, new_base: float) -> float:
    import math
    return log_value / math.log(new_base, 10)
