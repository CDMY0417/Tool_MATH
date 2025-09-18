def point_division_ratio(p1: tuple, p2: tuple, m: int, n: int):
    x1, y1 = p1
    x2, y2 = p2
    x = (m * x2 + n * x1) / (m + n)
    y = (m * y2 + n * y1) / (m + n)
    return (x, y)
