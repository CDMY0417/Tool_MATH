def simplify_fraction(numerator: str, denominator: str):
    if '(x+2)' in numerator and '(x+2)' in denominator:
        return numerator.replace('(x+2)', ''), denominator.replace('(x+2)', '')
    return numerator, denominator
