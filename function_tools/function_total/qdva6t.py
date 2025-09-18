def is_point_below_line(point: tuple, line_point1: tuple, line_point2: tuple) -> bool:
    x, y = point
    x1, y1 = line_point1
    x2, y2 = line_point2
    line_slope = (y2 - y1) / (x2 - x1)
    line_y_intercept = y1 - line_slope * x1
    return y < line_slope * x + line_y_intercept
