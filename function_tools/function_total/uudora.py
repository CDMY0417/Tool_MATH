def parse_polynomial(polynomial: str):
    import re
    terms = re.findall(r'([+-]?\d*)x\^?(\d*)', polynomial.replace(' ', ''))
    parsed_terms = []
    for coef, pow in terms:
        if coef == '' or coef == '+':
            coef = 1
        elif coef == '-':
            coef = -1
        else:
            coef = int(coef)
        pow = int(pow) if pow else (1 if 'x' in polynomial else 0)
        parsed_terms.append((coef, pow))
    return parsed_terms
