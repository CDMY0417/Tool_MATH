def substitute_expression(original_expr: str, sub_var: str, sub_expr: str) -> str:
    return original_expr.replace(sub_var, '(' + sub_expr + ')')
