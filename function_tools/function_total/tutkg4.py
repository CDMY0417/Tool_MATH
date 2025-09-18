def simplify_fraction(numerator: str, denominator: str):
    for term in denominator.split('*'):
        if term in numerator.split('*'):
            numerator = numerator.replace(term, '', 1)
            denominator = denominator.replace(term, '', 1)
    return numerator.strip('*'), denominator.strip('*')
