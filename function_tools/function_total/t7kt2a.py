def cross_multiply(frac1_num: str, frac1_den: str, frac2_num: str, frac2_den: str) -> str:
    lhs = f'({frac1_num}) * ({frac2_den})'
    rhs = f'({frac1_den}) * ({frac2_num})'
    return lhs + ' = ' + rhs
