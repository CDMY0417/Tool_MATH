def point_on_line(start: tuple, end: tuple, ratio: float):
    x = start[0] + (end[0] - start[0]) * ratio
    y = start[1] + (end[1] - start[1]) * ratio
    return (x, y)
