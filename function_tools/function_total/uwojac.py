def parabola_equation(vertex: tuple, point: tuple):
    h, k_y = vertex
    x, y = point
    k_value = x / ((y - k_y) ** 2)
    return f'x = {k_value}(y - {k_y})**2'
