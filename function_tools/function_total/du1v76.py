def is_point_on_line(point: tuple, point_a: tuple, point_b: tuple):
    return all((point[i] - point_a[i]) == (point_b[i] - point_a[i]) for i in range(len(point)))
