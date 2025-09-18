def add_equations(coeffs1: tuple, const1: int, coeffs2: tuple, const2: int):
    coeffs_result = tuple(c1 + c2 for c1, c2 in zip(coeffs1, coeffs2))
    const_result = const1 + const2
    return coeffs_result, const_result
