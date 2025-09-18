def y_value_from_slope_and_point(x: int, base_x: int, base_y: int, slope: float) -> int:
    delta_x = x - base_x
    return base_y + int(delta_x * slope)
