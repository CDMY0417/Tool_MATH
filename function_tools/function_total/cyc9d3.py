def substitute_variable(equation: str, variable: str, value: int) -> str:
    import re
    substituted = re.sub(rf'{variable}', str(value), equation)
    return substituted
