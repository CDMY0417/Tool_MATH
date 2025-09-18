def solve_linear_equations(equation1: tuple[float, float, float], equation2: tuple[float, float, float]):
    (a1, b1, c1), (a2, b2, c2) = equation1, equation2
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None  # No unique solution
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return (x, y)
