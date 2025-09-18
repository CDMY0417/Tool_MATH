def solve_linear_inequality(a: float, b: float, c: float):
    if a == 0:
        return None
    elif a > 0:
        return (-float('inf'), (c - b) / a)
    else:
        return ((c - b) / a, float('inf'))
