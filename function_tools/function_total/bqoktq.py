def parameterize_line(point1: tuple, point2: tuple, t: float) -> tuple:
    direction = (point2[0] - point1[0], point2[1] - point1[1])
    return (point1[0] + t * direction[0], point1[1] + t * direction[1])
