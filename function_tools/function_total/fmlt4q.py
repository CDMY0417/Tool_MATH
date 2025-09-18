def solve_linear_equations(equations: list[str]):
    from sympy import symbols, solve
    variables = symbols('a b c')
    solutions = solve(equations, variables)
    return solutions
