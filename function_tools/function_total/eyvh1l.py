def line_equation_given_slope(point: tuple, slope: float) -> str:
    x, y = point
    b = y - slope * x
    return f'y = {slope}x + {b}'
