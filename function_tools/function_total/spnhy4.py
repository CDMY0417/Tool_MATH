def cancel_common_factors(numerator: str, denominator: str):
    from sympy import simplify, symbols
    x = symbols('x')
    return simplify(numerator + '/' + denominator)
