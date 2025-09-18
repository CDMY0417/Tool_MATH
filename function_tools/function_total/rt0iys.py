def multiply_and_subtract_equations(coefficients_eq1: tuple, coefficients_eq2: tuple, constant1: int, constant2: int, results: tuple) -> int:
    result = constant1 * results[0] - constant2 * results[1]
    return result
