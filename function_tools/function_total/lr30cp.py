def substitute_expression(equation: str, variable: str, expression: str) -> str:
    return equation.replace(variable, '(' + expression + ')')
