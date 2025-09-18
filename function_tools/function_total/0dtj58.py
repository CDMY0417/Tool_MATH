def point_vector_form_to_slope_intercept(direction: tuple, point: tuple) -> tuple:
    A, B = direction
    x0, y0 = point
    m = -A / B
    b = (A * x0 + B * y0) / B
    return m, b
