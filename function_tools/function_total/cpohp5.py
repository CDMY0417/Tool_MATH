def largest_modular_value(base: int, step: int, upper_limit: int):
    m = (upper_limit - base) // step
    return base + m * step
