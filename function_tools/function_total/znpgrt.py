def substitute_variable(equation: str, variable: str, expression: str) -> str:
    return equation.replace(variable, f'({expression})')
