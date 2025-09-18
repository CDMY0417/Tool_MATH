def substitute_and_simplify(expression: str, equation: str, variable: str) -> str:
    import sympy as sp
    expr = sp.sympify(expression)
    eq = sp.sympify(equation)
    var = sp.symbols(variable)
    substituted_eq = eq.subs(var, expr)
    simplified_eq = sp.simplify(substituted_eq)
    return str(simplified_eq)
