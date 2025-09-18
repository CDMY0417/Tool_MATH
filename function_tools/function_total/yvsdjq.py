from sympy import symbols, Eq, solve

def solve_two_variable_system(equation1: tuple[float, float, float, float], equation2: tuple[float, float, float, float]) -> tuple:
    a, b = symbols('a b')
    eq1 = Eq(equation1[0]*a**2 + equation1[1]*b**2 + equation1[2]*b + equation1[3], 0)
    eq2 = Eq(equation2[0]*a**2 + equation2[1]*b**2 + equation2[2]*a + equation2[3], 0)
    solution = solve((eq1, eq2), (a, b))
    return solution[a], solution[b]
