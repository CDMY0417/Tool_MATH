def expand_root_formula(a: int, b: int, n: int):
    from sympy import sqrt, expand
    x = a + b * sqrt(2)
    return expand(x ** n)
