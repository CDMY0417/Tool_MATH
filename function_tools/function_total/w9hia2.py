def section_ratio_point(a: float, point_a: tuple, b: float, point_b: tuple):
    total = a + b
    x = (a * point_a[0] + b * point_b[0]) / total
    y = (a * point_a[1] + b * point_b[1]) / total
    return (x, y)
