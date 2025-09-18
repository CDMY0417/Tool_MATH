def line_equation_from_point_slope(point: tuple, slope: float):
    x0, y0 = point
    if slope == float('inf'):
        # Vertical line: x = x0 
        a, b, c = 1, 0, -x0
    else:
        a, b, c = -slope, 1, slope * x0 - y0
    return a, b, c
