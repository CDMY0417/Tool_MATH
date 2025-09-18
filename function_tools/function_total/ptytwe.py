def factor_out_root(polynomial: list[float], root: float) -> list[float]:
    quotient = []
    remainder = 0
    for coeff in polynomial:
        remainder = remainder * root + coeff
        quotient.append(remainder)
    return quotient[:-1]
