def solve_for_variable(equations: tuple, variable: str):
    from sympy import solve
    solution = solve(equations, variable)
    return solution[0]
