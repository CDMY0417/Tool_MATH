def evaluate_parabola(x: float, a: float, vertex: tuple, c: float):
    x_vertex, y_vertex = vertex
    y = a * (x - x_vertex) ** 2 + c
    return y
