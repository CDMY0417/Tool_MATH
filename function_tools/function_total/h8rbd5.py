def solve_linear_system_3x3(eq1: tuple[float, float, float, float], eq2: tuple[float, float, float, float], eq3: tuple[float, float, float, float]) -> tuple[float, float, float]:
    from sympy import symbols, Eq, solve
    x, y, z = symbols('x y z')
    equation1 = Eq(eq1[0] * x + eq1[1] * y + eq1[2] * z, eq1[3])
    equation2 = Eq(eq2[0] * x + eq2[1] * y + eq2[2] * z, eq2[3])
    equation3 = Eq(eq3[0] * x + eq3[1] * y + eq3[2] * z, eq3[3])
    solution = solve((equation1, equation2, equation3), (x, y, z))
    return solution[x], solution[y], solution[z]
