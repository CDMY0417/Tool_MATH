def multiply_polynomial_by_monomial(poly_coefficients: list[int], monomial_coefficient: int, monomial_degree: int) -> list[int]:
    return [monomial_coefficient * a for a in poly_coefficients] + [0] * monomial_degree
