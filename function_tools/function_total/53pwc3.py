def equation_solver_2x2(equation1: tuple[float, float, float], equation2: tuple[float, float, float]):
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return x, y
