def substitute_expression(expression: str, variable: str, equation: str) -> str:
    return equation.replace(variable, f'({expression})')
