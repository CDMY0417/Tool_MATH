def combine_like_terms(terms: list[str]) -> list[str]:
    coeffs = {}
    for term in terms:
        if 'x' in term:
            coeff = term.replace('x', '')
            if coeff in ('', '+'):
                coeff = '1'
            elif coeff == '-':
                coeff = '-1'
            coeff = int(coeff)
        else:
            coeff = int(term)
        power = 1 if 'x' in term else 0
        if power in coeffs:
            coeffs[power] += coeff
        else:
            coeffs[power] = coeff
    combined_terms = []
    for power, coeff in sorted(coeffs.items(), reverse=True):
        if power == 0:
            combined_terms.append(str(coeff))
        elif power == 1:
            combined_terms.append(f'{coeff}x')
    return combined_terms
