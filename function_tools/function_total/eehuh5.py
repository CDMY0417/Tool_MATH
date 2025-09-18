def simplify_linear_expression(coefficients: list[int], variable: str) -> str:
    total_coefficient = sum(coefficients)
    return f'{total_coefficient}{variable}'
