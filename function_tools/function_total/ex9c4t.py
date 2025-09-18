def divide_line_segment(point1: tuple, point2: tuple, ratio1: int, ratio2: int):
    x1, y1 = point1
    x2, y2 = point2
    x = (ratio1 * x2 + ratio2 * x1) / (ratio1 + ratio2)
    y = (ratio1 * y2 + ratio2 * y1) / (ratio1 + ratio2)
    return (x, y)
