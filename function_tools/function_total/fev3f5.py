def exponentiate_fraction(numerator: int, denominator: int, power: int):
    numer_exp = numerator ** power
    denom_exp = denominator ** power
    return (numer_exp, denom_exp)
