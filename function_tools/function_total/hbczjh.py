def substitute_variable(expr: str, old_var: str, new_expression: str) -> str:
    substituted_expr = expr.replace(old_var, new_expression)
    return substituted_expr
