def parabola_vertex_left_of_line(a: float, b: float, c: float, h: float) -> bool:
    vertex_x = -b / (2 * a)
    return vertex_x < h
