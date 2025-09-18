def calculate_expression_value(coefficients: tuple, variable_value: int):
    a, b, c = coefficients
    return a * variable_value + b == c
