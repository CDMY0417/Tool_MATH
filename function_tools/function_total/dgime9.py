def trig_sum_to_product(sin_coeff: float, cos_coeff: float, a: float) -> float:
    import math
    theta = math.atan2(sin_coeff, cos_coeff)
    amplitude = math.sqrt(sin_coeff**2 + cos_coeff**2)
    return amplitude * math.sin(a + theta)
