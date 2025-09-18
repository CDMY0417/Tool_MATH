def log_base_change(value: int, original_base: int, new_base: int):
    import math
    return math.log(value, new_base) / math.log(original_base, new_base)
