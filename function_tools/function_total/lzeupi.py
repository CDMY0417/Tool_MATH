def solve_linear_equations(equations: tuple[tuple[float, float, float], tuple[float, float, float]]) -> tuple[float, float]:
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(equations[0][0] * x + equations[0][1] * y, equations[0][2])
    eq2 = Eq(equations[1][0] * x + equations[1][1] * y, equations[1][2])
    solution = solve((eq1, eq2), (x, y))
    return solution[x], solution[y]
