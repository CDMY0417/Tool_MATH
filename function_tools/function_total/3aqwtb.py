def sum_of_variables(coefficients: list[float], variables: list[float]) -> float:
    return sum(c * v for c, v in zip(coefficients, variables))
