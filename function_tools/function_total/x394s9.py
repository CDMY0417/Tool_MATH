def power_of_point_equation(product: int, distance: int):
    from sympy import symbols, Eq, solve
    x = symbols('x', real=True)
    eq = Eq(x * (distance + x), product)
    solutions = solve(eq, x)
    return [sol.evalf() for sol in solutions if sol.evalf() > 0]
