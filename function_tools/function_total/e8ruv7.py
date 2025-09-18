def perform_polynomial_division(dividend_coeffs: list[float], divisor_coeffs: list[float]):
    from sympy import Poly, symbols
    x = symbols('x')
    p1 = Poly(dividend_coeffs[::-1], x)
    p2 = Poly(divisor_coeffs[::-1], x)
    quotient, remainder = p1.div(p2)
    return quotient.all_coeffs()[::-1], remainder.all_coeffs()[::-1]
