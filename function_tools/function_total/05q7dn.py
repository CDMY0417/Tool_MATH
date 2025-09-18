def solve_system_of_linear_equations(equation1: tuple[float, float, float], equation2: tuple[float, float, float]):
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(equation1[0] * x + equation1[1] * y, equation1[2])
    eq2 = Eq(equation2[0] * x + equation2[1] * y, equation2[2])
    solution = solve((eq1, eq2), (x, y))
    return solution
