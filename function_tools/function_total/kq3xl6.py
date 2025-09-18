def substitute_expression(equation: str, variable: str, expression: str):
    return equation.replace(variable, f'({expression})')
