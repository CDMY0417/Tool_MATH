def parameterize_line(point1: tuple, point2: tuple, t: float):
    x = point1[0] + (point2[0] - point1[0]) * t
    y = point1[1] + (point2[1] - point1[1]) * t
    z = point1[2] + (point2[2] - point1[2]) * t
    return (x, y, z)
