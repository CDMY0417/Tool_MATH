def solve_linear_system(equation1: tuple, equation2: tuple) -> tuple:
    from sympy import symbols, Eq, solve
    a, b = symbols('a b')
    eq1 = Eq(equation1[0] * a + equation1[1] * b, equation1[2])
    eq2 = Eq(equation2[0] * a + equation2[1] * b, equation2[2])
    solution = solve((eq1, eq2), (a, b))
    return solution[a], solution[b]
