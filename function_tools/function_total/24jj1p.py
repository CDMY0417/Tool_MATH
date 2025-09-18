def compute_complex_angle(angle: float):
    import math
    cos_value = round(math.cos(math.radians(angle)), 10)
    sin_value = round(math.sin(math.radians(angle)), 10)
    return complex(cos_value, sin_value)
