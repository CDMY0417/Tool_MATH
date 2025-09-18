def substitute_and_simplify(expr: str, substitutions: dict) -> str:
    for var, value in substitutions.items():
        expr = expr.replace(var, str(value))
    return expr
