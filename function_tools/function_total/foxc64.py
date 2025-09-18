def sum_to_product_sin(angle_a: float, angle_b: float):
    from math import sin, cos, radians
    return 2 * sin(radians((angle_a + angle_b) / 2)) * cos(radians((angle_a - angle_b) / 2))
