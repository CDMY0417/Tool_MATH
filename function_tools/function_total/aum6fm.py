def solve_quadratic_inequality(a: int, b: int, c: int):
    from sympy import symbols, solve
    x = symbols('x')
    expr = a*x**2 + b*x + c
    critical_points = solve(expr, x)
    solution_intervals = []
    left_sign = expr.subs(x, critical_points[0] - 1)
    if left_sign < 0:
        solution_intervals.append((-float('inf'), critical_points[0]))
    between_sign = expr.subs(x, (critical_points[0] + critical_points[1]) / 2)
    if between_sign < 0:
        solution_intervals.append((critical_points[0], critical_points[1]))
    right_sign = expr.subs(x, critical_points[1] + 1)
    if right_sign < 0:
        solution_intervals.append((critical_points[1], float('inf')))
    return solution_intervals
