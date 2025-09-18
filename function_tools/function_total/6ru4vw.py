def solve_linear_equations(a: int, b: int, c: int, d: int, e: int, f: int):
    determinant = a * d - b * c
    x = (e * d - b * f) / determinant
    y = (a * f - e * c) / determinant
    return (x, y)
