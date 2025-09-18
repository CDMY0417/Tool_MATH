def substitute_variable(eq1: tuple, eq2: tuple, solve_var: str):
    if solve_var == 'x':
        a1, b1, c1 = eq1
        a2, b2, c2 = eq2
        new_eq = (b1, a1 * a2, b2 * a1)
    else:  # for 'y'
        a1, b1, c1 = eq1
        a2, b2, c2 = eq2
        new_eq = (a1, b1 * a2, b2 * b1)
    return new_eq
