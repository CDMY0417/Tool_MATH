def convert_log_base(value: float, original_base: float, new_base: float) -> float:
    import math
    return math.log(value, original_base) / math.log(new_base, original_base)
