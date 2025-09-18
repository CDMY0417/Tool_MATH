def product_to_sum(a: float, b: float) -> float:
    from math import sin, cos
    return 0.5 * (cos(a - b) - cos(a + b))
