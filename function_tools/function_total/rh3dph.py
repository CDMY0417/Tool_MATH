def quadratic_inequality_solution(a: float, b: float, c: float):
    # This function assumes a != 0
    from sympy import symbols, solve, Interval, Union
    x = symbols('x')
    expr = a * x**2 + b * x + c
    solutions = solve(expr > 0, x)
    intervals = Union(*solutions)
    return intervals
