def multiply_equation(factor: int, lhs: str, rhs: str):
    new_lhs = f'({factor}) * ({lhs})'
    new_rhs = f'({factor}) * ({rhs})'
    return new_lhs, new_rhs
