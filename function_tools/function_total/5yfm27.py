def center_of_line_segment(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    x_center = (point1[0] + point2[0]) / 2
    y_center = (point1[1] + point2[1]) / 2
    return (x_center, y_center)
