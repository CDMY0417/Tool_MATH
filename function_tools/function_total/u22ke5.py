def solve_linear_equations(equation1: tuple[float, float, float], equation2: tuple[float, float, float]) -> tuple[float, float]:
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2
    if b2 != 0:
        x = (c1 - b1 * (c2 / b2)) / (a1 - b1 * (a2 / b2))
        y = (c2 - a2 * x) / b2
    else:
        y = (c1 - a1 * (c2 / a2)) / (b1 - a1 * (b2 / a2))
        x = (c2 - b2 * y) / a2
    return x, y
