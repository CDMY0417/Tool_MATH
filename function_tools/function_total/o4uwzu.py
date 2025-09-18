def solve_linear_equations(a1: float, b1: float, c1: float, a2: float, b2: float, c2: float):
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None  # No unique solution
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return x, y
