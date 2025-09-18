def solve_linear_system(coefficients: list[list[float]], constants: list[float]):
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(coefficients[0][0]*x + coefficients[0][1]*y, constants[0])
    eq2 = Eq(coefficients[1][0]*x + coefficients[1][1]*y, constants[1])
    sol = solve((eq1, eq2), (x, y))
    return sol[x], sol[y]
