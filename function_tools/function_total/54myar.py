def format_polynomial(coefficients: list[int]) -> str:
    terms = []
    degree = len(coefficients) - 1
    for i, coeff in enumerate(coefficients):
        if coeff == 0:
            continue
        if degree - i == 0:
            terms.append(f'{coeff}')
        elif degree - i == 1:
            terms.append(f'{coeff}x')
        else:
            terms.append(f'{coeff}x^{degree - i}')
    return ' + '.join(terms) if terms else '0'
