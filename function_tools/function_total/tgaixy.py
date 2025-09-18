def solve_linear_inequality(inequality: str):
    import sympy as sp
    x = sp.symbols('x')
    solution = sp.solve(inequality, x)
    return solution
