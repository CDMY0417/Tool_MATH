def solve_exponential_equation(a: int, b: int):
    from sympy import symbols, Eq, solve, log
    x = symbols('x')
    equation = Eq(a**x, b)
    sol = solve(equation, x)
    return sol[0] if sol else None
