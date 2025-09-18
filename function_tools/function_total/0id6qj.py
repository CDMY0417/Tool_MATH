def solve_inequality_greater_than(numerator: str, denominator: str, constant: float):
    from sympy import symbols, solve
    x = symbols('x')
    inequality = f'({numerator})/({denominator}) - {constant} > 0'
    solution = solve(inequality, x)
    return solution
