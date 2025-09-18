def sum_of_coefficients_of_degree(polynomial: dict[int, float], degree: int) -> float:
    return sum(coefficient for deg, coefficient in polynomial.items() if deg == degree)
