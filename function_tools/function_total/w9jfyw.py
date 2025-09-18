def substitute_variable(expression: str, subst: dict):
    for old, new in subst.items():
        expression = expression.replace(old, new)
    return expression
