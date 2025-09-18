def evaluate_linear_combination(coefficients: list[float], variables: list[float]) -> float:
    return sum(coef * var for coef, var in zip(coefficients, variables))
