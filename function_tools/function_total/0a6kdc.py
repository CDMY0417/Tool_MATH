def maximize_quadratic(a: float, b: float, c: float, min_x: float, max_x: float) -> float:
    vertex_x = -b / (2*a)
    if min_x <= vertex_x <= max_x:
        return a*vertex_x**2 + b*vertex_x + c
    else:
        value_at_min = a*min_x**2 + b*min_x + c
        value_at_max = a*max_x**2 + b*max_x + c
        return max(value_at_min, value_at_max)
