def simplify_fraction(numerator: str, denominator: str):
    num_terms = numerator.split('*') if '*' in numerator else [numerator]
    den_terms = denominator.split('*') if '*' in denominator else [denominator]
    for term in num_terms.copy():
        if term in den_terms:
            num_terms.remove(term)
            den_terms.remove(term)
    simplified_num = '*'.join(num_terms)
    simplified_den = '*'.join(den_terms)
    return (simplified_num, simplified_den)
