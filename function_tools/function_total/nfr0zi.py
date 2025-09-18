def factor_expression(coefficients: list[int], powers: list[int]):
    from math import gcd
    import sympy as sp
    x = sp.symbols('x')
    gcf = gcd(*coefficients)
    min_power = min(powers)
    new_coefficients = [c // gcf for c in coefficients]
    new_powers = [p - min_power for p in powers]
    factored_exp = gcf * x**min_power * sum(nc * x**np for nc, np in zip(new_coefficients, new_powers))
    return factored_exp
